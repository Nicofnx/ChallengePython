from fastapi import FastAPI, HTTPException
import sqlite3
from models.field import InputData
from database.database import conn, cursor


app = FastAPI()

# Conectar a la base de datos SQLite
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


# Ruta para procesar las peticiones POST
@app.post("/input/{my_target_field}")
async def process_input_data(my_target_field: str, data: InputData):
    # Verificar si my_target_field es uno de los campos permitidos
    allowed_fields = ["field_1", "author", "description"]
    if my_target_field not in allowed_fields:
        raise HTTPException(status_code=400, detail= my_target_field + " no es válido o no es posible convertir a mayúscula")

    # Convertir el texto del campo especificado a mayúsculas
    field_data = getattr(data, my_target_field).upper()
    setattr(data, my_target_field, field_data)

    # Guardar el JSON modificado en la base de datos
    query = "INSERT INTO documents (field_1, author, description, my_numeric_field) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (data.field_1, data.author, data.description, data.my_numeric_field))
    conn.commit()

    # Obtener el ID del documento recién guardado
    document_id = cursor.lastrowid

    return {"id": document_id}

# Ruta para obtener datos por ID
@app.get("/get_data/{id}")
async def get_data(id: int):
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
