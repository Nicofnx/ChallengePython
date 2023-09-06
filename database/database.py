import sqlite3

# Conecto a la base de datos SQLite (si no existe, se creará)
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Creo la tabla "documents" si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        field_1 TEXT,
        author TEXT,
        description TEXT,
        my_numeric_field INTEGER
    )
""")

# Guardo los cambios 
conn.commit()

# Cierro la conexión
conn.close()
