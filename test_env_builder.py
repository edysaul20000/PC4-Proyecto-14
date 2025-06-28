import sys
import os
import subprocess


def start_test_env(nombre_entorno, lista_variables):
    print(f"Iniciando entorno de prueba: {nombre_entorno}")
    entorno = os.environ.copy()

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


def main():
    argumentos = sys.argv[1:]

    if not argumentos:
        return

    comando = argumentos[0]

    if comando == "start_test_env" and len(argumentos) >= 2:
        nombre_entorno = argumentos[1]
        lista_variables = argumentos[2:]
        start_test_env(nombre_entorno, lista_variables)


if __name__ == '__main__':
    main()
