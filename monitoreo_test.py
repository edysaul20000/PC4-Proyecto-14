import os
import datetime
import json
import glob

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


# mostrar el historial de ejecuciones, mostrando las ultimas 5 ejecuciones
def mostrar_historico():
    archivos = sorted(glob.glob(os.path.join(results_dir, "metricas_*.json")))[-5:]
    print("\n" + "*************************")
    print("las ultimas 5 ejecuciones:")
    print("*************************")
    exitos = fallos = 0

    for archivo in archivos:
        m = leer_metricas(archivo)
        if m:
            estado = "OK" if m.get('exito') else "FALLO"
            print(f"{estado} {m['timestamp']} ({m['duracion_segundos']}s)")
            exitos += 1 if m.get('exito') else 0
            fallos += 0 if m.get('exito') else 1

    print(f"\nresumen: {exitos} exitos, {fallos} fallos")
    print("=" * 50)


# generar metricas de la ejecucion, guardando un archivo json con el resultado
def generar_metricas(exito, duracion, log_text, run_id):
    metricas = {
        "timestamp": run_id,
        "exito": exito,
        "duracion_segundos": round(duracion, 2),
        "ambiente": os.getenv("CI_ENVIRONMENT_NAME", "local"),
        "build_id": os.getenv("GITHUB_RUN_NUMBER", "unknown"),
        "detalles": log_text[:500]
    }

    metricas_file = os.path.join(results_dir, f"metricas_{run_id}.json")
    with open(metricas_file, "w") as f:
        json.dump(metricas, f, indent=2)

    return metricas_file
