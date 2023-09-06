# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Copia todo el contenido de la aplicación al contenedor
COPY . .

# Expone el puerto 5000 para que la aplicación FastAPI escuche
EXPOSE 5000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
