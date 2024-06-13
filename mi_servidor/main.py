from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola! servidor de prueba de la clase de Esp. en desarrollo Web!"}

@app.get("/search")
async def root(busqueda:str):
    return f"La búsqueda es: '{busqueda}'"

@app.get("/saludar/{nombre}")
async def root(nombre:str):
    return f'Hola, {nombre}, ¿Cómo estás?. \n Este es el servidor de Bruno.'

@app.get("/obtenermayor")
async def root(num1:int, num2:int):
    numeroMayor=None
    if num1 > num2: 
        numeroMayor = num1
    elif num1 < num2:
        numeroMayor = num2
    else:
        return 'Los números son iguales.'    
    return f'El número mayor es {numeroMayor}'