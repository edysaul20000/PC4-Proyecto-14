import os
import datetime


results_dir = "resultados"
logs_dir = os.path.join(results_dir, "logs")
reports_dir = os.path.join(results_dir, "reports")

tests_dir = os.path.join("services", "microservice", "tests")

def crear_carpetas():
    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")