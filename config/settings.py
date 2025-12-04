# config/settings.py
# Configuración centralizada de la aplicación

import os
from typing import Dict, Any


class Settings:
    """Configuración de la aplicación"""
    
    # Configuración del servidor
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    RELOAD: bool = True
    
    # Configuración de batalla por defecto
    DEFAULT_ROUNDS: int = 3
    DEFAULT_TOPIC: str = "Quién domina más el escenario"
    
    # Pesos por defecto para puntuación
    DEFAULT_SCORING_WEIGHTS: Dict[str, float] = {
        'rhyme': 0.25,
        'metric': 0.20,
        'attack': 0.25,
        'sentiment': 0.20,
        'penalty': -0.10
    }
    
    # Configuración de APIs externas
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    
    # Configuración de moderación
    MODERATION_LEVEL: str = os.getenv("MODERATION_LEVEL", "medium")
    JUDGE_STRICT_MODE: bool = os.getenv("JUDGE_STRICT_MODE", "false").lower() == "true"
    
    @classmethod
    def load_from_env(cls) -> 'Settings':
        """Cargar configuración desde variables de entorno"""
        return cls()


# Instancia global de configuración
settings = Settings.load_from_env()
