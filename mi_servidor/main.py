from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola! servidor de prueba de la clase de Esp. en desarrollo Web!"}



@app.get("/saludar/{nombre}")
async def root(nombre:str):
    return f'Hola, {nombre}, ¿Cómo estás?. \n Este es el servidor de Bruno.'

