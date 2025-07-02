import os
import datetime
import json


results_dir = "resultados"
logs_dir = os.path.join(results_dir, "logs")
reports_dir = os.path.join(results_dir, "reports")

tests_dir = os.path.join("services", "microservice", "tests")


# crear carpetas de resultados, donde se guardarán los logs y reportes
def crear_carpetas():
    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)


def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def guardar_archivo(path, contenido, descripcion="archivo"):
    with open(path, "w") as f:
        f.write(contenido)
    print(f"{descripcion} guardado en {path}")


def leer_metricas(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
