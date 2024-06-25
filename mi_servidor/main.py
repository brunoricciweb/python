from fastapi import FastAPI
# from pydantic import BaseModel
from validations import Product




app = FastAPI()

products = [
    Product(id=1,nombre='Yerba sin palo', categoria='alimentos', precio=1234.55),
    Product(id=2,nombre='Queso cremoso', categoria='lacteos', precio=3566.00),
]


def filtrarPorCategoria(listaProductos, cat):
    output = []
    for p in listaProductos:
        if p['categoria'] == cat: 
            output.append(p)
    return output

def filtrarPorId(listaProductos, id):
    for p in listaProductos:
        if p.id == id: 
            return p   # devuelve el producto y sale de la función

def validarId(listaProductos, id):
    for p in listaProductos:
        if p.id == id: 
            return False
    return True


@app.get("/")
async def root():
    return {"message": "Hola! servidor de prueba de la clase de Esp. en desarrollo Web!"}

@app.get("/search")
async def search(busqueda:str):
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


#######################################

@app.post("/producto")  # POST -> crear producto
async def root(newProduct: Product) -> dict:
    print('Los datos del producto son:', newProduct)
    if(validarId(products, newProduct.id)):
        products.append( newProduct )
        return {'message': 'Se creó el producto'}
    else:
        return {'message': f'No se pudo crear el producto. El id {newProduct.id} ya existe.'}


@app.get("/productos/{category}")  # GET -> obtener productos
async def root(category:str):
    print(f'Se filtra por la categoría {category}')
    return filtrarPorCategoria(products, category)

@app.get("/productos")  # GET -> obtener productos
async def root() -> list[Product]:
    return products

@app.get("/producto/{id}")  # obtiene el producto según su ID
async def root(id:int) -> Product:
    resultado = filtrarPorId(products, id)
    if resultado == None: 
        return f'No existe el producto con ID {id}'
    else: 
        return resultado 

