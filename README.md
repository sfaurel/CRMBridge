# CMR Bridge

## Descripción
Prueba técnica para postular a vacante de de desarrollador backend.

Consiste en implementar una API Flask en un para manejar solicitudes de usuarios, realizar consultas a una base de datos y consumir datos desde una API de CRM.

### Rutas
- **`/`** o **`/api`**: Proporciona la documentación de la API, describiendo los endpoints disponibles, sus parámetros y respuestas.
- **`/status/`**: Retorna un JSON con el estado del servicio.
- **`/users/`**: Creación y listado de usuarios.
- **`/auth/`**: Endpoint dedicado a la autenticación.
- **`/leads/`**: Creación y listado de leads.


### Configuración
1. Clonar el proyecto
    ```bash
    git clone https://github.com/sfaurel/CRMBridge.git
    ```

2. Crear un archivo `.env` en la raíz del proyecto, incluir las siguientes variables:
    ```env
    FLASK_ENV=development
    SECRET_KEY=<your_secret_key>
    STREAK_API_KEY=<your_streak_api_key>
    STREAK_API_URL=https://api.streak.com/api
    ```
    **SECRET_KEY**: cadena de texto aleatoria, es la llave que se utilizara para cifrar el token de autenticación, es importante que esta llave no se filtre, cualquiera con acceso a esta llave podrá crear crear un JWT falso y acceder a la API sin necesidad de la contraseña.

    **STREAK_API_KEY**: token para acceder a la API de streak CRM.

3. Crear y activar un entorno virtual, luego instalar las dependencias:
    ```bash
    python -m venv venv #crear entorno virtual
    source venv/bin/activate #activar entorno virtual
    pip install -r requirements.txt #instalar dependencias
    ```
4. Iniciar la base de datos.

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. Ejecutar la aplicación:
    ```bash
    python run.py
    ```

6. Conectarse al servicio a través del navegador.
    ```bash
    http://localhost:5000
    ```
    