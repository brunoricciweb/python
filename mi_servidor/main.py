from fastapi import FastAPI

app = FastAPI()

products = [
    {
        "id": 1,
    "nombre": "Yerba sin palo",
    "categoria": "alimentos",
    "precio": 5670
  },
  {
    "id": 2,
    "nombre": "Yogurt",
    "categoria": "lacteos",
    "precio": 4200
  },
   {
    "id": 3,
    "nombre": "Queso Provolone",
    "categoria": "lacteos",
    "precio": 7433
  },  
    {
    "id": 4,
    "nombre": "Manzana roja",
    "categoria": "frutas",
    "precio": 1610
  }
]


def filtrarPorCategoria(listaProductos, cat):
    output = []
    for p in listaProductos:
        if p['categoria'] == cat: 
            output.append(p)
    return output

def filtrarPorId(listaProductos, id):
    for p in listaProductos:
        if p['id'] == id: 
            return p   # devuelve el producto y sale de la función


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
async def root(product:dict):
    print('Los datos del producto son:', product)
    products.append( product )
    return {'message': 'Se creó el producto'}

@app.get("/productos/{category}")  # GET -> obtener productos
async def root(category:str):
    print(f'Se filtra por la categoría {category}')
    return filtrarPorCategoria(products, category)

@app.get("/productos")  # GET -> obtener productos
async def root():
    return products

@app.get("/producto/{id}")  # obtiene el producto según su ID
async def root(id:int):
    resultado = filtrarPorId(products, id)
    if resultado == None: 
        return f'No existe el producto con ID {id}'
    else: 
        return resultado 

