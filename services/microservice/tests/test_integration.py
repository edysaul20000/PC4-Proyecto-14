import subprocess
import time
import uuid
import pytest
import requests

# URL base del microservicio cuando se ejecuta en el entorno de prueba
MICROSERVICE_URL = "http://localhost:8000"


@pytest.fixture(scope="function")
def test_env(request):
    """
    Fixture de pytest que levanta y destruye un entorno de prueba Docker
    para un modulo de pruebas completo.
    """
    # genera un nombre de proyecto unico
    env_name = f"test-env-{uuid.uuid4().hex[:8]}"
    # leemos la configuracion del mock desde el decorador @pytest.mark.mock_config
    marker = request.node.get_closest_marker("mock_config")
    env_vars = [f"{k}={v}" for k, v in marker.kwargs.items()] if marker else []

    start_command = ["python", "../../../test_env_builder.py",
                     "start_test_env", env_name] + env_vars
    try:
        print(f"\n Levantando entorno de prueba: {env_name} con config: {env_vars}")
        subprocess.run(start_command, check=True, capture_output=True, text=True)
        time.sleep(5)
        yield
    finally:
        print(f"\n Destruyendo entorno de prueba: {env_name}")
        stop_command = ["python", "../../../test_env_builder.py", "stop_test_env", env_name]
        subprocess.run(stop_command, check=True, capture_output=True, text=True)


@pytest.mark.mock_config(MOCK_RESPONSE_TYPE="success")
def test_get_data_success(test_env):
    """
    Prueba de integracion para el escenario de exito.
    Verifica que el microservicio procesa correctamente una respuesta exitosa del mock.
    """
    response = requests.get(f"{MICROSERVICE_URL}/data")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Datos obtenidos exitosamente desde el mock."
    assert data["mock_response"]["status"] == "active"


@pytest.mark.mock_config(MOCK_RESPONSE_TYPE="error")
def test_get_data_with_mock_error(test_env):
    """
    Prueba de integración para el escenario de error.
    Verifica que el microservicio maneja un error 500 del mock y devuelve un 503.
    """
    response = requests.get(f"{MICROSERVICE_URL}/data")
    assert response.status_code == 503
    data = response.json()
    assert "Error al comunicarse con el servicio externo" in data["detail"]
