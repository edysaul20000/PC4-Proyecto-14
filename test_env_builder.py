import sys
import os
import subprocess
import yaml


def start_test_env(nombre_entorno, lista_variables, escenario_path=None):
    print(f"Iniciando entorno de prueba: {nombre_entorno}")
    entorno = os.environ.copy()

    # Si se especifica un escenario, cargar variables de entorno desde el archivo YAML
    if escenario_path:
        with open(escenario_path, 'r') as f:
            escenario = yaml.safe_load(f)
        for servicio, config in escenario.get('services', {}).items():
            for k, v in config.get('env', {}).items():
                entorno[k] = v
                print(f"   -> [escenario] {servicio}: {k}={v}")

    # Variables de entorno adicionales por CLI
    for variable in lista_variables:
        if '=' in variable:
            clave, valor = variable.split('=', 1)
            entorno[clave] = valor
            print(f"   -> Configurando variable: {clave}={valor}")
        else:
            print(f"Advertencia: La variable '{variable}'"
                  "no tiene el formato CLAVE=VALOR y sera ignorada.")

    comando = [
        'docker', 'compose',
        '--project-name', nombre_entorno,
        'up',
        '--build',
        '-d'
    ]

    try:
        subprocess.run(comando, check=True, env=entorno)
        print(f"Entorno '{nombre_entorno}' iniciado correctamente.")
    except subprocess.CalledProcessError as error:
        print(f"Error al iniciar el entorno: {error}")
    except FileNotFoundError:
        print("Error: 'docker compose' no se encuentra.")


def stop_test_env(nombre_entorno):
    print(f"Deteniendo entorno de prueba: {nombre_entorno}")

    comando = [
        'docker', 'compose',
        '--project-name', nombre_entorno,
        'down'
    ]

    try:
        subprocess.run(comando, check=True)
        print(f"Entorno '{nombre_entorno}' detenido y eliminado.")
    except subprocess.CalledProcessError as error:
        print(f"Error al detener el entorno: {error}")
    except FileNotFoundError:
        print("Error: 'docker compose' no se encuentra.")


def main():
    argumentos = sys.argv[1:]

    if not argumentos:
        return

    comando = argumentos[0]

    if comando == "start_test_env":
        nombre_entorno = argumentos[1]
        # Buscar si se pasa --scenario <archivo>
        escenario_path = None
        if '--scenario' in argumentos:
            idx = argumentos.index('--scenario')
            escenario_path = argumentos[idx + 1]
            lista_variables = argumentos[2:idx]
        else:
            lista_variables = argumentos[2:]
        start_test_env(nombre_entorno, lista_variables, escenario_path)
    elif comando == "stop_test_env" and len(argumentos) == 2:
        nombre_entorno = argumentos[1]
        stop_test_env(nombre_entorno)


if __name__ == '__main__':
    main()