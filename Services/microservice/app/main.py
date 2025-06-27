from fastapi import FastAPI
import requests
import os

app = FastAPI()

MOCK_URL = os.getenv("MOCK_URL", "http://localhost:5001/mock-response")

@app.get("/data")
def get_data():
    try:
        response = requests.get(MOCK_URL)
        response.raise_for_status()
        mock_data = response.json()
        return {
            "message": "Datos obtenidos exitosamente desde el mock.",
            "mock_response": mock_data
        }
    except Exception as e:
        return {
            "error": "No se pudo obtener respuesta del mock.",
            "details": str(e)
        }