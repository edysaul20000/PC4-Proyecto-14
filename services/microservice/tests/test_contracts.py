import requests
import json
import os
import pytest
from jsonschema import validate
import subprocess
import time
import uuid

# Cargar el esquema JSON desde archivo
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "contract_response_schema.json")
with open(SCHEMA_PATH) as f:
    RESPONSE_SCHEMA = json.load(f)

MICROSERVICE_URL = "http://localhost:8000/data"
MOCK_URL = "http://localhost:5001/mock-response"


@pytest.fixture(scope="function")
def test_env():
    """
    Fixture que levanta y destruye un entorno de prueba Docker para pruebas de contrato.
    """
    env_name = f"test-contracts-{uuid.uuid4().hex[:8]}"
    start_command = ["python", "../../../test_env_builder.py", "start_test_env", env_name]
    try:
        subprocess.run(start_command, check=True, capture_output=True, text=True)
        time.sleep(5)
        yield
    finally:
        stop_command = ["python", "../../../test_env_builder.py", "stop_test_env", env_name]
        subprocess.run(stop_command, check=True, capture_output=True, text=True)


def test_mock_contract(test_env):
    """
    El mock debe cumplir con el contrato de respuesta definido en el JSON Schema.
    """
    response = requests.get(MOCK_URL)
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=RESPONSE_SCHEMA)


def test_microservice_contract(test_env):
    """
    El microservicio debe cumplir con el contrato de respuesta para el campo 'mock_response'.
    """
    response = requests.get(MICROSERVICE_URL)
    assert response.status_code == 200
    data = response.json()
    # Validar solo el campo mock_response
    assert "mock_response" in data
    validate(instance=data["mock_response"], schema=RESPONSE_SCHEMA)
