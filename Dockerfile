# Usa una imagen base de Python
FROM python:3.12.2

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt y otros archivos necesarios para instalar las dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto que usará la aplicación
EXPOSE 4000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]