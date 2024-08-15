## Iniciar proyecto de FastAPI

1) Crear carpeta vacía
2) Abrir la terminal en el directorio de la carpeta creada
3) Crear entorno virtual de python
    > python -m venv myvenv
4) Activar entorno creado
    > source myvenv/bin/activate
5) Instalar dependencias
    > pip install --only-binary :all: fastapi[all]
6) Generar archivo `requirements.txt` 

    **Nota:** cada vez que se instalen dependencias nuevas, correr este comando para mantener actualizado el archivo de dependencias
    > pip freeze > requirements.txt

---
### Correr proyecto ya existente:
1) Clonar el repositorio
2) Crear entorno virtual
3) Activar entorno virtual 
**Nota:** en caso de ya contar con el archivo  `requirements.txt` instalar las dependencias automáticamente con el comando:
    > pip install -r requirements.txt

## Iniciar el servidor 
Con la terminal en el directorio del proyecto: _El nombre `main.py` corresponde al archivo que contiene el programa principal_
> fastapi dev main.py

Para poder probar el servidor usando ThunderClient o Postman, es necesario exponer el puerto en el que corre el servidor (por defecto, puerto 8000)
- En la terminal ir a la pestaña "puertos" o "ports".
- Seleccionar puerto 8000, clic derecho, visibilidad -> Public
    ![image](https://github.com/user-attachments/assets/f379f55f-1d06-4a47-b5ca-7a2b40acea83)