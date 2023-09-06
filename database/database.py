import sqlite3

# Conectar a la base de datos SQLite (si no existe, se creará)
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Crear la tabla "documents" si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        field_1 TEXT,
        author TEXT,
        description TEXT,
        my_numeric_field INTEGER
    )
""")

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()
