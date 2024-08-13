## Iniciar proyecto de FastAPI

1) Crear carpeta vacía
2) Abrir la terminal en el directorio de la carpeta creada
3) Crear entorno virtual de python
    > python -m venv myvenv
4) Activar entorno creado
    > source myvenv/bin/activate
5) Instalar dependencias
    > pip install fastapi
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