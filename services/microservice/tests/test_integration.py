import subprocess
import time
import uuid
import pytest

@pytest.fixture(scope="function")
def test_env(request):
    """
    Fixture de pytest que levanta y destruye un entorno de prueba Docker
    para un módulo de pruebas completo.
    """
    # genera un nombre de proyecto unico
    env_name = f"test-env-{uuid.uuid4().hex[:8]}"
    
    # leemos la configuracion del mock desde el decorador @pytest.mark.mock_config
    marker = request.node.get_closest_marker("mock_config")
    env_vars = [f"{k}={v}" for k, v in marker.kwargs.items()] if marker else []

    start_command = ["python", "../../../test_env_builder.py", "start_test_env", env_name] + env_vars
    
    try:
        print(f"\n Levantando entorno de prueba: {env_name} con config: {env_vars}")
        subprocess.run(start_command, check=True, capture_output=True, text=True)
        time.sleep(5)
        yield
    finally:
        print(f"\n Destruyendo entorno de prueba: {env_name}")
        stop_command = ["python", "../../../test_env_builder.py", "stop_test_env", env_name]
        subprocess.run(stop_command, check=True, capture_output=True, text=True)
