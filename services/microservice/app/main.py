from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

MOCK_URL = os.getenv("MOCK_URL", "http://localhost:5001/mock-response")


@app.get("/data")
def get_data():
    try:
        response = requests.get(MOCK_URL, timeout=10)
        response.raise_for_status()
        mock_data = response.json()
        return {
            "message": "Datos obtenidos exitosamente desde el mock.",
            "mock_response": mock_data
        }
    except requests.exceptions.RequestException as e:
        # Si hay un error de red o un error HTTP del mock, devolvemos un 503
        raise HTTPException(
            status_code=503,
            detail=f"Error al comunicarse con el servicio externo: {e}"
        )
