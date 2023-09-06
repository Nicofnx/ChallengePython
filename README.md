# ChallengePython
# Mi Aplicación FastAPI

Esta es una aplicación FastAPI simple que permite realizar operaciones CRUD en una base de datos SQLite y requiere autenticación básica. Puedes usar este README para obtener información sobre cómo configurar y ejecutar la aplicación.

## Crear un Entorno Virtual de Prueba

Para crear un entorno virtual de Python y preparar tu entorno de prueba, sigue estos pasos:

1. Abre una terminal en la ubicación de tu proyecto.

2. Ejecuta el siguiente comando para crear un entorno virtual llamado "myenv" (puedes cambiar el nombre si lo deseas):

   python -m venv myenv

Activa el entorno virtual:

En Windows:

myenv\Scripts\activate

En macOS y Linux:

source myenv/bin/activate

Una vez activado el entorno virtual, instala las dependencias requeridas utilizando pip:

pip install -r requirements.txt

Ejecutar la Aplicación
Para ejecutar la aplicación, sigue estos pasos:

Asegúrate de tener el entorno virtual activado.

Desde la raíz del proyecto, ejecuta el siguiente comando:

uvicorn main:app --host 0.0.0.0 --port 5000
Esto iniciará la aplicación FastAPI en el puerto 5000.
La direccion que te dara para abir sera http://localhost:5000
Para utilizar swagger coloca docs al final de la url: http://localhost:5000/docs

## Uso de la Aplicación
Una vez que la aplicación esté en funcionamiento, puedes utilizarla para realizar las siguientes acciones:

1. Autenticación Básica
La aplicación requiere autenticación básica. Utiliza las siguientes credenciales para autenticarte:

Usuario: admin
Contraseña: 1234

2. Crear un Nuevo Documento
Puedes crear un nuevo documento enviando una solicitud POST a la siguiente URL:

http://localhost:5000/input/{my_target_field}
Asegúrate de reemplazar {my_target_field} con uno de los siguientes valores: "field_1", "author" o "description". La solicitud debe incluir un JSON en el cuerpo con los campos correspondientes.
Utiliza swagger para una mejor vizualizacion.

3. Obtener Datos por ID
Puedes obtener datos de un documento por su ID enviando una solicitud GET a la siguiente URL:

http://localhost:5000/get_data/{id}
Reemplaza {id} con el ID del documento que deseas obtener.

Contribuciones
Si deseas contribuir a esta aplicación o informar sobre problemas, siéntete libre de abrir un problema o enviar una solicitud de extracción en el repositorio de GitHub.
