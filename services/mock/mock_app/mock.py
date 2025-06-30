from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import uvicorn
import time

app = FastAPI()


@app.get("/mock-response")
def mock_response():
    response_type = os.getenv("MOCK_RESPONSE_TYPE", "success")

    if response_type == "error":
        return JSONResponse(
            status_code=500,
            content={"error": "ERROR: Respuesta de error simulada"},
            media_type="application/json"
        )
    
    if response_type == "delay":
        try:
            delay_seconds = int(os.environ.get("MOCK_DEMORA_SEGUNDOS", "5"))
            time.sleep(delay_seconds)
        except (ValueError, TypeError):
            time.sleep(5)
            
    return {
            "user_id": 123,
            "status": "active",
            "message": "Respuesta de exito simulada",
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
