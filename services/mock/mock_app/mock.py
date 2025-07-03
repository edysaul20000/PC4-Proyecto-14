from fastapi import FastAPI, Response
import json
import os
import uvicorn
import time

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'datasets')


@app.get("/mock-response")
def mock_response():
    response_type = os.getenv("MOCK_RESPONSE_TYPE", "success")
    data_file = os.getenv("MOCK_DATA_FILE", "success.json")
    file_path = os.path.join(DATASETS_DIR, data_file)

    if not os.path.exists(file_path):
        return Response(content=json.dumps(
            {"error": f"Archivo de datos no encontrado: {data_file}"}),
            status_code=404, media_type="application/json")

    with open(file_path, 'r') as f:
        data = json.load(f)

    if response_type == "success":
        return Response(content=json.dumps(data), status_code=200, media_type="application/json")
    elif response_type == "error":
        return Response(content=json.dumps(data), status_code=500, media_type="application/json")
    elif response_type == "latency":
        time.sleep(5)
        return Response(content=json.dumps(data), status_code=200, media_type="application/json")
    else:
        return Response(content=json.dumps({"error": "Tipo de respuesta no valida"}),
                        status_code=400)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
