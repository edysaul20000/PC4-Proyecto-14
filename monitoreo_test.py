import os
import datetime
import json
import glob
import subprocess
import time
import sys


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
        "detalles": log_text[:]
    }

    metricas_file = os.path.join(results_dir, f"metricas_{run_id}.json")
    with open(metricas_file, "w") as f:
        json.dump(metricas, f, indent=2)

    return metricas_file


# ejecutar los tests y generar un reporte HTML
def ejecutar_tests(html_file):
    print("**************************************")
    print("ejecutando Test")
    print("**************************************")

    try:
        resultado = subprocess.run(
            [
                "pytest",
                "--maxfail=1",
                "-q",
                f"--html={html_file}",
                "--self-contained-html"
            ],
            cwd=tests_dir,
            capture_output=True,
            text=True,
            check=False
        )

        salida = resultado.stdout.strip()
        errores = resultado.stderr.strip()
        salida_completa = f"{salida}\n{errores}".strip()

        return resultado.returncode == 0, salida_completa

    except FileNotFoundError:
        return False, "error: no se encontro 'pytest'"


def main():
    crear_carpetas()
    run_id = timestamp()

    log_file = os.path.abspath(os.path.join(logs_dir, f"run_{run_id}.log"))
    html_file = os.path.abspath(os.path.join(reports_dir, f"run_{run_id}.html"))
    alerta_file = os.path.abspath(os.path.join(results_dir, f"alerta_{run_id}.txt"))

    inicio = time.time()
    exito, log_text = ejecutar_tests(html_file)
    duracion = time.time() - inicio

    guardar_archivo(log_file, log_text, "log")
    metricas_file = generar_metricas(exito, duracion, log_text, run_id)
    mostrar_historico()

    if exito:
        print("todos los tests pasaron")
        print(f"report html: {html_file}")
        print(f"metricas: {metricas_file}")
        sys.exit(0)
    else:
        print("los test fallaron")
        print("la alerta se esta generando")
        guardar_archivo(alerta_file, f"tests fallaron:\n\n{log_text}", "alerta")
        sys.exit(1)


if __name__ == "__main__":
    main()
