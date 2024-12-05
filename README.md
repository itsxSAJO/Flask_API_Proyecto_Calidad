# REST API con Python, Flask y PostgreSQL

REST API con Python, Flask y PostgreSQL. Usaremos el protocolo HTTP junto con los métodos GET, POST, PUT y DELETE y el formato JSON para enviar y recibir datos; además, aprende a probarla utilizando un cliente REST como Insomnia.

## 1. Crear un entorno virtual

Primero, crea un entorno virtual ejecutando el siguiente comando:

```bash
python -m virtualenv env
```

## 2. Instalar los paquetes necesarios

Para instalar los paquetes necesarios, ejecuta:

```bash
pip install -r requirements.txt
pip install flask flask-cors psycopg2 python-decouple python-dotenv 
```

## 3. Crear un archivo .env

Crea un archivo .env en la raíz del proyecto con las siguientes variables de entorno:


```ini
SECRET_KEY=SECRET_KEY
PGSQL_HOST=host
PGSQL_USER=user
PGSQL_PASSWORD=password
PGSQL_DB=database

```

## 4. Ejecutar el entorno virtual y el archivo app.py
```bash
.\env\Scripts\activate
python .\src\app.py
```
