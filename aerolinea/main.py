from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola! servidor de prueba de la clase de Esp. en desarrollo Web!"}