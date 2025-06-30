# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiamos los archivos del microservicio
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./mock_app .

# Exponer el puerto
EXPOSE 5001

# Este comando inicia el servidor FastAPI
CMD ["uvicorn", "mock:app", "--host", "0.0.0.0", "--port", "5001"]