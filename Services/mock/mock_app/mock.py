from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import uvicorn

app = FastAPI()

@app.get("/mock-response")
def mock_response():
    response_type = os.getenv("MOCK_RESPONSE_TYPE", "success")

    if response_type == "error":
        return JSONResponse(
            status_code=500, 
            content={"error": "Simulated error response"}
        )
    else:
        return {
            "user_id": 123,
            "status": "active",
            "message": "Simulated success response"
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)