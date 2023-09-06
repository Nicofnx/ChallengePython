from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import sqlite3
from models.field import InputData
from database.database import conn, cursor

import sqlite3

# Conecto a la base de datos SQLite (si no existe, se creará)
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

app = FastAPI()
security = HTTPBasic()

# Función para verificar las credenciales de autenticación
def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == "admin" and credentials.password == "1234":
        return True
    return False

# Ruta para procesar las peticiones (Metodo POST)
@app.post("/input/{my_target_field}")
async def process_input_data(
    my_target_field: str,
    data: InputData,
    is_authenticated: bool = Depends(verify_credentials)  # Verifico las credenciales aquí
  ):
    # Verifico si el usuario está autenticado
    if not is_authenticated:
        raise HTTPException(status_code=401, detail="Autenticación fallida")

    # Verifico si my_target_field es uno de los campos permitidos
    allowed_fields = ["field_1", "author", "description"]
    # Si no es un campo permitido arrojo de lanza un error
    if my_target_field not in allowed_fields:
        raise HTTPException(status_code=400, detail= my_target_field + " no es válido o no es posible convertir a mayúscula")

    # Convierto el texto del campo especificado a mayúsculas acorde a si el campo es author o field 1
    field_data = getattr(data, my_target_field).upper()
    setattr(data, my_target_field, field_data)

    # Guardo el JSON modificado en la base de datos
    query = "INSERT INTO documents (field_1, author, description, my_numeric_field) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (data.field_1, data.author, data.description, data.my_numeric_field))
    conn.commit()

    # Obtengo el ID del ultimo documento guardado
    document_id = cursor.lastrowid

    return {"id": document_id}

# Ruta para obtener datos por ID (metodo GET)
@app.get("/get_data/{id}")
async def get_data(
    id: int,
    is_authenticated: bool = Depends(verify_credentials)
  ):

    if not is_authenticated:
        raise HTTPException(status_code=401, detail="Autenticación fallida")
    query = "SELECT field_1, author, description, my_numeric_field FROM documents WHERE ID = ?"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    data = {
        "ID": id,
        "field_1": result[0],
        "author": result[1],
        "description": result[2],
        "my_numeric_field": result[3],
    }
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
