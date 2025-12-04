# tests/conftest.py
# Configuración común para los tests con pytest

import pytest
from fastapi.testclient import TestClient
import sys
import os

# Añadir el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.battle_api import app


@pytest.fixture
def client():
    """Cliente de prueba para la API"""
    return TestClient(app)


@pytest.fixture
def sample_battle_request():
    """Datos de ejemplo para una batalla"""
    return {
        "topic": "Quién domina el escenario",
        "rounds": 2,
        "persona_A_id": "fast_technical",
        "persona_B_id": "punchline_master"
    }


@pytest.fixture
def sample_personas():
    """Personalidades de ejemplo"""
    from personas.personas import RAPPER_PERSONAS
    return RAPPER_PERSONAS
