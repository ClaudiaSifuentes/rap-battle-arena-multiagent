# api/llm_client.py

import os
import json
import textwrap
from typing import Optional, Dict, List

import boto3



MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")

BEDROCK_REGION = os.getenv("AWS_REGION", "us-east-1")


bedrock_runtime = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)


def build_rapper_prompt(
    persona: Dict,
    topic: str,
    last_opponent_verse: Optional[str] = None,
    max_lines: int = 4,
    max_words_per_line: int = 11,
) -> str:
    """
    Construye el prompt para el rapero, usando la personalidad + contexto.
    """
    style_desc = persona.get("style_description", "")
    name = persona.get("name", "Rapero de batalla")

    base_instruction = f"""
    Eres un rapero de batalla en español llamado "{name}".
    Tu estilo es el siguiente: {style_desc}

    Estás en una batalla tipo torneo internacional de freestyle,
    similar a una God Level, frente a público en vivo.

    Tema de la ronda: "{topic}".

    Escribe un verso en español, competitivo, con rimas y punchlines creativas,
    atacando al rival de forma ingeniosa, pero SIN insultos explícitos,
    SIN contenido discriminatorio y evitando lenguaje de odio.

    Reglas de formato:
    - Máximo {max_lines} líneas.
    - Cada línea con menos de {max_words_per_line} palabras.
    - No expliques nada, responde SOLO con el verso.
    """

    if last_opponent_verse:
        base_instruction += f"""

        Este fue el verso anterior del oponente, respóndele directamente:

        \"\"\"{last_opponent_verse}\"\"\"
        """

    prompt = textwrap.dedent(base_instruction).strip()
    return prompt


def postprocess_verse(
    raw_text: str,
    max_lines: int = 4,
    max_words_per_line: int = 11,
) -> str:
    """
    Limpia la salida del modelo:
    - Se queda con máximo max_lines líneas.
    - Recorta cada línea a max_words_per_line palabras.
    """
    lines = [l.strip() for l in raw_text.split("\n") if l.strip()]

    if len(lines) == 1:
        parts = []
        for chunk in lines[0].split("."):
            chunk = chunk.strip()
            if chunk:
                parts.append(chunk)
        if parts:
            lines = parts

    lines = lines[:max_lines]

    processed_lines: List[str] = []
    for line in lines:
        words = line.split()
        if len(words) > max_words_per_line:
            words = words[:max_words_per_line]
        processed_lines.append(" ".join(words))

    return "\n".join(processed_lines).strip()


def generate_verse_llm(
    persona: Dict,
    topic: str,
    last_opponent_verse: Optional[str] = None,
    max_lines: int = 4,
    max_words_per_line: int = 11,
    max_tokens: int = 256,
    temperature: float = 0.8,
) -> str:
    """
    Genera un verso usando AWS Bedrock (Claude 3 Haiku como ejemplo).
    """
    prompt = build_rapper_prompt(
        persona=persona,
        topic=topic,
        last_opponent_verse=last_opponent_verse,
        max_lines=max_lines,
        max_words_per_line=max_words_per_line,
    )

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ],
            }
        ],
    }

    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    response_body = json.loads(response["body"].read())

    raw_text = ""
    if "content" in response_body and response_body["content"]:
        for block in response_body["content"]:
            if block.get("type") == "text":
                raw_text += block.get("text", "") + "\n"

    raw_text = raw_text.strip()

    if not raw_text:
        return "No tengo palabras, pero esta batalla sigue encendida."

    clean_verse = postprocess_verse(
        raw_text=raw_text,
        max_lines=max_lines,
        max_words_per_line=max_words_per_line,
    )
    return clean_verse
