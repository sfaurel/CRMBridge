# CMR Bridge

## Descripción
Prueba para postular a vacante de de desarrollador backend.

### Rutas
- **`/status/`**: Retorna un JSON con el estado del servicio.

### Configuración
1. Crear un archivo `.env` en la raíz del proyecto, incluir las siguientes variables:
    ```env
    FLASK_ENV=development
    ```

2. Crear y activar un entorno virtual, luego instalar las dependencias:
    ```bash
    python -m venv venv #crear entorno virtual
    source venv/bin/activate #activar entorno virtual
    pip install -r requirements.txt #instalar dependencias
    ```

3. Ejecutar la aplicación:
    ```bash
    python run.py
    ```
