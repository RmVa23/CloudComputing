# Imagen base oficial de Python
FROM python:3.9
EXPOSE 8080

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de dependencias e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Indica cómo iniciar la aplicacion
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
