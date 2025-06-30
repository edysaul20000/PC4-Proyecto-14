# Grupo 6 - PC4-Proyecto-14

## Team

| Miembro del Equipo | Codigo |
| :----------------- | :-------------------- | 
| **Choquecambi Germain** | `20211360A` |
| **Serrano Edy** | `20211229B` | 
| **Hinojosa Frank** | `20210345I`  | 

## Descripcion

**[Proyecto 14 - Grupo 6](https://github.com/edysaul20000/PC4-Proyecto-14)**, desarrollar una herramienta robusta para la creacion de entornos de prueba aislados y altamente configurables. Aprovechando Docker Compose para orquestar servicios y mocks de API, permitiendo simular dependencias externas de manera eficiente y controlada. Enfocado en facilitar el testing de microservicios, asegurando que las pruebas sean consistentes, repetibles y no dependan de servicios externos reales.usando:

- Git hooks
- Scripts python
- Mocks y simuladores
- Docker

## Flujo de Trabajo
Se utilizo la estrategia **Git Flow** para organizar el desarrollo:

- **Ramas principales**:
  - `main`: Contiene la version estable y lista para produccion.
  - `develop`: Integra las funcionalidades completadas antes de pasar a `main`.

- **Ramas de soporte**:
  - `feature/*`: Cada nueva funcionalidad o issue se desarrolla en una rama `feature/nombre-issue` creada desde `develop`.
  - `hotfix/*`: Para corregir errores críticos detectados en `main`.
  - `release/*`: Preparacion de nuevas versiones antes de fusionar a `main`.

## Estructura del Proyecto

```
PC4-Proyecto-14/
├── docker-compose.yaml          # Orquestación de servicios
├── test_env_builder.py         # CLI para gestión de entornos
├── .env                        # Variables de entorno
├── services/
│   ├── microservice/           # Microservicio FastAPI
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── app/
│   │       └── main.py         # Aplicación principal
│   └── mock/                   # Mock Service
│       ├── Dockerfile
│       ├── requirements.txt
│       └── mock_app/
│           └── mock.py         # Simulador de API
└── services/hooks/
    └── pre-commit             # Git hook de validación
```

**El avance se ha divido en 3 Sprints**

## Sprint 1

Realizado del 27 al 28 de junio de 2025, se compone de los siguiente:

### 1. Ramas

- `feature/microservice-basic`, desarrollado por **Edy Serrano** 
- `ffeature/microservice-docker`, desarrollado por **Edy Serrano** 
- `feature/microservice-mock`, desarrollado por **Frank Hinojosa** 
- `feature/mock-docker`, desarrollado por **Frank Hinojosa** 
- `feature/docker-compose`, desarrollado por **Germain Choquechambi** 
- `feature/pre-commit`, desarrollado por **Germain Choquechambi** 
- `feature/test-env-builder`, desarrollado por **Germain Choquechambi** 

### 2. Issues

- [#1](#1-implementar-microservicio-basico) Implementar microservicio basico
- [#2](#2-dockerizar-un-microservicio) Dockerizar un microservicio 
- [#5](#5-crear-mock-de-api-externa-con-respuesta-simulada) Crear mock de API externa con respuesta simulada
- [#6](#6-dockerizar-el-mock) Dockerizar el mock
- [#9](#9-docker-compose-para-microservicio-y-mock) Docker-compose para microservicio y mock
- [#10](#10-hook-pre-commit-para-validar-docker-compose-y-flake8) Docker-compose para microservicio y mock
- [#13](#13-cli-python-para-iniciardetener-entornos-con-variables) CLI Python para iniciar/detener entornos con variables

### 3. Pull Request

- [#3](https://github.com/edysaul20000/PC4-Proyecto-14/pull/3) : merge[#1]: Feature/microservice-basic a develop
- [#4](https://github.com/edysaul20000/PC4-Proyecto-14/pull/4) : merge[#2]:Feature/microservice-docker a develop 
- [#7](https://github.com/edysaul20000/PC4-Proyecto-14/pull/7) : merge[#5]: Feature/microservice-mock a develop
- [#8](https://github.com/edysaul20000/PC4-Proyecto-14/pull/8) : merge[#6]: Feature/mock-docker a develop 
- [#11](https://github.com/edysaul20000/PC4-Proyecto-14/pull/11) : merge[#5]: Feature/docker compose a develop
- [#12](https://github.com/edysaul20000/PC4-Proyecto-14/pull/12) : merge[#10]: Feature/pre-commit a develop
- [#14](https://github.com/edysaul20000/PC4-Proyecto-14/pull/14) : merge[#13]: Feature/test env builder



## Objetivos

Desarrollar una herramienta para orquestar servicios con Docker Compose y configurar sus comportamientos básicos.

**Enunciado:**    
* Define un **microservicio de ejemplo** que dependa de un servicio externo (ej. una API de terceros, una base de datos) y un mock/simulador para esa dependencia.
* Crea archivos **`docker-compose.yaml`** para el microservicio y el mock.
* Desarrolla una herramienta CLI en Python (`test_env_builder.py`) que:
     * `start_test_env <env_name>`: Inicia los servicios Docker Compose para un entorno de prueba.
    * `stop_test_env <env_name>`: Detiene y elimina el entorno.
    * Permita pasar **variables de entorno** a los servicios para configurar su comportamiento (ej. URL del mock).
* Implementa **Git Hooks** (`pre-commit`) para validar la sintaxis de los archivos Docker Compose.

## Demostracion en video

[Sprint 1 (29/06/2025) Grupo 6 Proyecto 14 ](https://www.youtube.com/watch?v=A_aYCbtDJuc&ab_channel=SerranoArosteguiEdySaul)

## Distribución

- **Edy Serrano**: Issues [#1](#1-implementar-microservicio-basico), [#2](#2-dockerizar-un-microservicio)
- **Frank Hinojosa**: Issues [#5](#5-crear-mock-de-api-externa-con-respuesta-simulada), [#6](#6-dockerizar-el-mock)
- **Germain Choquecambi**: [#9](#9-docker-compose-para-microservicio-y-mock), [#10](#10-hook-pre-commit-para-validar-docker-compose-y-flake8), [#13](#13-cli-python-para-iniciardetener-entornos-con-variables)

## Issues del Sprint 1

### [#1](https://github.com/edysaul20000/PC4-Proyecto-14/issues/1) Implementar microservicio basico
- **User story**  
    **As a** desarrollador
    **I need** crear un microservicio basico que exponga una API HTTP con al menos una ruta que se comunique con un servicio externo (mock)
    **So that** pueda simular la logica de negocio de una aplicacion que depende de un servicio
- **Responsable**: Edy Serrano
- **Rama**: `feature/microservice-basic`
- **Objetivo**: Crear un microservicio basico en Python que exponga una API HTTP y se conecte exitosamente a un mock de servicio externo usando una URL configurable por variable de entorno retornando una respuesta que incluya la información del mock

### [#2](https://github.com/edysaul20000/PC4-Proyecto-14/issues/2) Dockerizar un microservicio  
- **User story**  
    **As a** desarrollador
    **I need** crear un Dockerfile que permita empaquetar y ejecutar el microservicio de forma aislada  
    **So that** pueda ser levantado en un entorno controlado y orquestado con Docker Compose
- **Responsable**: Edy Serrano
- **Rama**: `ffeature/microservice-docker`
- **Objetivo**: Crear un Dockerfile funcional para el microservicio que permita construir una imagen Docker, la cual al ejecutarse, inicie correctamente el microservicio y lo haga accesible para recibir peticiones HTTP, garantizando su aislamiento y preparacion para orquestacion con Docker Compose.

### [#5](https://github.com/edysaul20000/PC4-Proyecto-14/issues/5) Crear mock de API externa con respuesta simulada
- **User story**  
    **As a** developer  
    **I need** construir un servicio mock que emule el comportamiento bAsico de una API externa  
    **So that** el microservicio de ejemplo pueda realizar pruebas sin depender de un servicio real
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/microservice-mock`
- **Objetivo**: Construir un servicio mock HTTP que simule una API externa en un endpoint fijo (/mock-response), capaz de devolver datos simulados.

### [#6](https://github.com/edysaul20000/PC4-Proyecto-14/issues/6) Dockerizar el mock
- **User story**  
    **As a** developer  
    **I need** empaquetar el mock en un contenedor Docker y permitir que su respuesta se pueda modificar mediante una variable de entorno  
    **So that** pueda usarse en pruebas automatizadas y orquestarse junto al microservicio
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/mock-docker`
- **Objetivo**: Crear un Dockerfile para el servicio mock que lo empaquete en un contenedor, permitiendo que su comportamiento de respuesta (exito o error) sea dinamicamente configurable en tiempo de ejecución a traves de la variable de entorno MOCK_RESPONSE_TYPE.

### [#9](https://github.com/edysaul20000/PC4-Proyecto-14/issues/9) Docker-compose para microservicio y mock
- **User story**  
    **As a** _Desarrollador_  
    **I need** _un archivo docker-compose.yaml que orqueste el microservicio y el mock como contenedores interconectados_  
    **So that** _puedan probarse juntos como si estuvieran en produccion, sin depender de servicios reales_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/docker-compose`
- **Objetivo**: Crear un archivo docker-compose.yaml que orqueste y conecte el microservicio y el mock en una red compartida, permitiendo que sus configuraciones se pasen a traves de variables de entorno.

### [#10](https://github.com/edysaul20000/PC4-Proyecto-14/issues/10) Hook pre-commit para validar docker-compose y flake8
- **User story**  
    **As a** _Desarrollador_  
    **I need** _ validar automaticamente los archivos `docker-compose` y el codigo Python antes de hacer commit_  
    **So that** _se eviten errores de sintaxis y se garantice que el codigo cumple con el estandar antes de integrarlo al repositorio_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/pre-commit`
- **Objetivo**: Implementar un Git pre-commit hook personalizado que valide automaticamente la sintaxis de los archivos docker-compose.yaml usando docker compose config y el código Python con flake8.


### [#13](https://github.com/edysaul20000/PC4-Proyecto-14/issues/13) CLI Python para iniciar/detener entornos con variables
- **User story**  
    **As a** _Desarrollador_  
    **I need** _una herramienta CLI que me permita iniciar o detener entornos de prueba, aceptando variables de entorno opcionales_ 
    **So that** _pueda configurar rapidamente distintos entornos de testing sin editar manualmente archivos_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/test-env-builder`
- **Objetivo**: Desarrollar una herramienta CLI (test_env_builder.py) que permita iniciar (start_test_env) y detener (stop_test_env) entornos de prueba orquestados con Docker Compose.

## Sprint 2

Realizado del 28 al 29 de junio de 2025, se compone de los siguiente:

### 1. Ramas

- `feature/answer-mock`, desarrollado por **Edy Serrano** 
- `feature/error-mock`, desarrollado por **Frank Hinojosa** 
- `feature/latencia-mock`, desarrollado por **Germain Choquechambi** 

### 2. Issues

- [#16](#16-probar-la-integracion-con-respuesta-exitosa-del-mock) Probar la integracion con respuesta exitosa del mock
- [#18](#18-probar-la-integracion-con-respuesta-de-error-del-mock) Probar la integracion con respuesta de error del mock
- [#20](#20-probar-la-integración-con-respuesta-lenta-del-mock) Probar la integración con respuesta lenta del mock

### 3. Pull Request

- [#19](https://github.com/edysaul20000/PC4-Proyecto-14/pull/19) : merge[#16]: Feature/answer-mock a develop
- [#21](https://github.com/edysaul20000/PC4-Proyecto-14/pull/21) : merge[#18]: Feature/error-mock a develop
- [#22](https://github.com/edysaul20000/PC4-Proyecto-14/pull/22) : merge[#20]: feature/latencia-mock a develop

## **Objetivo:** 
Permitir la configuración detallada de los mocks y ejecutar pruebas que interactúen con ellos.

**Enunciado:**
* Mejora el mock/simulador de la dependencia externa para que su comportamiento pueda ser **configurado dinámicamente** (ej. a través de un archivo JSON, variables de entorno, o una API en el propio mock). Esto permitirá simular diferentes escenarios (respuestas exitosas, errores, latencia).
* Extiende la CLI para que pueda pasar configuraciones detalladas a los mocks al iniciar el entorno.
* Desarrolla **pruebas de integración** con `pytest` para el microservicio de ejemplo, que:
    * Utilicen la CLI para levantar el entorno de prueba.
    * Configuren el mock para un escenario específico.
    * Ejecuten llamadas al microservicio y verifiquen que interactúa correctamente con el mock configurado.
* Aplica **principios SOLID aplicados a tests** al diseñar las pruebas, enfocándose en el aislamiento y la independencia.

## Demostracion en video

[Sprint 2 (30/06/2025) Grupo 6 Proyecto 14 ](https://www.youtube.com/watch?v=VM09BMjrsps&ab_channel=SerranoArosteguiEdySaul)

## Distribución

- **Edy Serrano**: Issues [#16](#16-probar-la-integracion-con-respuesta-exitosa-del-mock)
- **Frank Hinojosa**: Issues [#18](#18-probar-la-integracion-con-respuesta-de-error-del-mock)
- **Germain Choquecambi**: [#20](#20-probar-la-integración-con-respuesta-lenta-del-mock)

## Issues del Sprint 2

### [#16](https://github.com/edysaul20000/PC4-Proyecto-14/issues/16) Probar la integracion con respuesta exitosa del mock
- **User story**  
    **As a** desarrollador  
    **I need** verificar que el microservicio procesa correctamente una respuesta exitosa de la dependencia externa simulada (mock)  
    **So that** pueda asegurar que el flujo principal de la aplicacion funciona como se espera.
- **Responsable**: Edy Serrano
- **Rama**: `feature/answer-mock`
- **Objetivo**: Validar que el microservicio pueda manejar de forma correcta una respuesta exitosa de una dependencia externa simulada.

### [#18](https://github.com/edysaul20000/PC4-Proyecto-14/issues/18) Probar la integracion con respuesta de error del mock
- **User story**  
    **As a** desarrollador  
    **I need** verificar que el microservicio maneja de forma controlada una respuesta de error de la dependencia externa simulada (mock)  
    **So that** pueda garantizar que el servicio es resiliente y comunica los fallos de sus dependencias de manera adecuada
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/error-mock`
- **Objetivo**: Asegurar que el microservicio pueda manejar correctamente los errores de sus dependencias externas, respondiendo de forma controlada y comunicando los fallos adecuadamente

### [#20](https://github.com/edysaul20000/PC4-Proyecto-14/issues/20) Probar la integración con respuesta lenta del mock
- **User story**  
    **As a** desarrollador  
    **I need** verificar que el microservicio puede manejar una respuesta con latencia de la dependencia externa simulada (mock) sin fallar  
    **So that** pueda asegurar que el servicio es robusto y no sufre de timeouts prematuros ante dependencias lentas.
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/latencia-mock`
- **Objetivo**: Confirmar que el microservicio pueda soportar y procesar respuestas lentas de sus dependencias externas sin fallar ni experimentar timeouts inesperados

## Sprint 3

Realizado del 29 al 30 de junio de 2025, se compone de los siguiente:

### 1. Ramas

- `feature/Orquestacion-prueba`, desarrollado por **Edy Serrano** 
- `release/sprint3`, desarrollado por **Frank Hinojosa** 
- `feature/prueba-contrato`, desarrollado por **Germain Choquechambi** 

### 2. Issues

- [#25](#25-implementación-de-pruebas-de-contrato-entre-microservicio-y-mock) Implementación de pruebas de contrato entre microservicio y mock
- [#26](#26-orquestacion-de-entornos-de-prueba-con-multiples-servicios-y-mocks) Orquestacion de Entornos de Prueba con Multiples Servicios y Mocks
- [#27](#27-implementar-reportes-de-pruebas-y-flujo-gitops-para-configuración-de-escenarios) Implementar Reportes de Pruebas y Flujo GitOps para Configuración de Escenarios

### 3. Pull Request

- [#28](https://github.com/edysaul20000/PC4-Proyecto-14/pull/28) : merge[#26]: Feature/orquestacion-prueba a develop
- [#29](https://github.com/edysaul20000/PC4-Proyecto-14/pull/29) : merge[#25]: Feature/prueba-contrato a develop

## **Objetivo:** 
 Implementar pruebas de contrato para las interacciones con los mocks y simular escenarios de prueba más complejos.
 
 **Enunciado:**
* Implementa **pruebas de contrato** para la interfaz entre el microservicio y el mock. Estas pruebas deben asegurar que el microservicio y el mock cumplen con una especificación de API acordada (ej. usando `pytest-contract` o validación de JSON Schema para las respuestas).
    
* Desarrolla un mecanismo para definir **escenarios de prueba complejos** que involucren múltiples servicios y mocks, y que el constructor de entornos pueda levantar y ejecutar de forma orquestada.
* Añade la capacidad de generar **reportes de ejecución de pruebas** detallados.
* Considera la implementación de un **GitOps simulado** para mantener los archivos de configuración de los entornos de prueba sincronizados.

## Demostracion en video

[Sprint 3 (30/06/2025) Grupo 6 Proyecto 14 ](https://www.youtube.com/watch?v=eJllHcq7G-k&ab_channel=SerranoArosteguiEdySaul)

## Distribución

- **Edy Serrano**: Issues [#25](#25-implementación-de-pruebas-de-contrato-entre-microservicio-y-mock)
- **Frank Hinojosa**: Issues [#27](#27-implementar-reportes-de-pruebas-y-flujo-gitops-para-configuración-de-escenarios)
- **Germain Choquecambi**: [#26](#26-orquestacion-de-entornos-de-prueba-con-multiples-servicios-y-mocks)

## Issues del Sprint 3

### [#25](https://github.com/edysaul20000/PC4-Proyecto-14/issues/25) Implementación de pruebas de contrato entre microservicio y mock
- **User story**  
    **As a** developer  
    **I need** implementar pruebas de contrato para la interfaz entre el microservicio y el mock  
    **So that** pueda asegurar que ambos servicios cumplen con una especificacion de API acordada y evitar errores de integracion  
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/prueba-contrato`
- **Objetivo**: Asegurar que ambos servicios cumplen con una especificacion de API acordada y evitar errores de integracion 

### [#26](https://github.com/edysaul20000/PC4-Proyecto-14/issues/26) Orquestacion de Entornos de Prueba con Multiples Servicios y Mocks
- **User story**  
    **As a** developer  
    **I need** desarrollar un mecanismo para definir escenarios de prueba que involucren multiples servicios y mocks, y que el constructor de entornos pueda levantarlos y ejecutarlos de forma orquestada
    **So that** pueda simular y validar situaciones reales de integracion entre varios microservicios y dependencias.
- **Responsable**: Edy Serrano
- **Rama**: `feature/Orquestacion-prueba`
- **Objetivo**: Validar situaciones reales de integracion entre varios microservicios y dependencias

### [#27](https://github.com/edysaul20000/PC4-Proyecto-14/issues/27) Implementar Reportes de Pruebas y Flujo GitOps para Configuración de Escenarios
- **User story**  
    **As a** desarrollador  
    **I need** añadir la capacidad de generar reportes de ejecución de pruebas detallados y mantener los archivos de configuración de los entornos de prueba sincronizados mediante un flujo GitOps simulado  
    **So that** pueda revisar fácilmente los resultados de las pruebas, compartir evidencia con el equipo y asegurar que todos trabajamos con los mismos escenarios validados  
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/latencia-mock`
- **Objetivo**: Revisar facilmente los resultados de las pruebas, compartir evidencia con el equipo y asegurar que todos trabajamos con los mismos escenarios validados

## Configuración Inicial

Para trabajar con el proyecto, realiza los pasos a continuacion.

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/edysaul20000/PC4-Proyecto-14.git
    cd PC4-Proyecto-14/
    ```

2. **Crear y activar el entorno virtual**
    ```bash
    python3 -m venv pc4
    source pc4/bin/activate
    ```

3. **Instalar dependencias**
    ```bash
    pip install -r services/microservice/requirements.txt 
    pip install -r  services/mock/requirements.txt 
    ```

4. **Instalar herramientas de analisis**

- Instalar flake8 para analizar codigo python
   
    ```bash
    pip install flake8
    ```

5. Copiar los hooks personalizados a la carpeta .git/hooks

    ```bash
    cp services/hooks/pre-commit .git/hooks/pre-commit
    ```

6. Dar permisos de ejecucion a los hooks 
    ```bash
    chmod +x .git/hooks/pre-commit
    ```

7. Ejecutar los tests de integracion

- Instalar pytest
    ```bash
    pip install pytest
    ```
- Movernos a la carpeta tests
    ```bash
    cd services/microservice/tests/
    ```

- Ejecutar el test_get_data_success
    ```bash
    pytest test_integration.py::test_get_data_success -v -s
    ```

- Ejecutar el test_get_data_with_mock_error
    ```bash
    pytest test_integration.py::test_get_data_with_mock_error -v -s
    ```

- Ejecutar el test_get_data_with_mock_delay
    ```bash
    pytest test_integration.py::test_get_data_with_mock_delay -v -s
    ```

- Ejecutar todo los tests
    ```bash
    pytest
    ```

8. Automatizacion de Entornos de Prueba con `test_env_builder.py`

- Instalar dependencia
   ```bash
    pip install jsonschema
    ```

- Flujo General

    ```bash
    python test_env_builder.py start_test_env <nombre_entorno> --scenario <ruta_yaml>
    # ...ejecuta tus pruebas...
    python test_env_builder.py stop_test_env <nombre_entorno>
    ```
- Escenario de Exito

    ```bash
    python test_env_builder.py start_test_env demo-success --scenario scenarios/success_simple.yaml
    # ...ejecuta tus pruebas...
    python test_env_builder.py stop_test_env demo-success
    ```

- Escenario con Mock que Responde con Error

    ```bash
    python test_env_builder.py start_test_env demo-error --scenario scenarios/error_mock.yaml
    # ...ejecuta tus pruebas...
    python test_env_builder.py stop_test_env demo-error
    ```
---

- Escenario con Latencia Simulada

    ```bash
    python test_env_builder.py start_test_env demo-delay --scenario scenarios/success_with_delay.yaml
    # ...ejecuta tus pruebas...
    python test_env_builder.py stop_test_env demo-delay
    ```

9. Generacion de Reportes

- Instalar dependencias
    ```bash
    pip install pytest-html
    ```
- Generacion de reporte
    ```bash
    pytest --html=report.html --self-contained-html
    ```
---

## Formas de Ejecutar el Proyecto

### Opción 1: Usando Docker Compose

**Iniciar entorno con CLI:**
```bash
# Entorno exitoso
python3 test_env_builder.py start_test_env demo-success MOCK_RESPONSE_TYPE=success

# Detener entorno exitoso
python3 test_env_builder.py stop_test_env demo-success

# Entorno con errores
python3 test_env_builder.py start_test_env demo-error MOCK_RESPONSE_TYPE=error

# Detener entorno con errores
python3 test_env_builder.py stop_test_env demo-error
```

**O directamente con Docker Compose:**
```bash
# Iniciar servicios
docker compose up --build

# Detener servicios
docker compose down
```

### Opción 2: Usando uvicorn individualmente

**Terminal 1 - Mock Service:**
```bash
# Respuesta exitosa
MOCK_RESPONSE_TYPE=success uvicorn services.mock.mock_app.mock:app --host 0.0.0.0 --port 5001 --reload

# Respuesta de error
MOCK_RESPONSE_TYPE=error uvicorn services.mock.mock_app.mock:app --host 0.0.0.0 --port 5001 --reload
```

**Terminal 2 - Microservicio:**
```bash
MOCK_URL=http://localhost:5001/mock-response uvicorn services.microservice.app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Probar los Servicios

```bash
# Probar microservicio
curl http://localhost:8000/data

# Probar mock directamente
curl http://localhost:5001/mock-response
