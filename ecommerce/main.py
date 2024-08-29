from fastapi import FastAPI, Request,Response
from sqlmodel import Field, Session, SQLModel, create_engine, select, delete

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from db import Product, create_db_and_tables, engine, readAllProducts, createProduct, deleteProduct,upsertCartProduct,getCart,deletCartProduct


app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

################## Interfaz gráfica ######################
# ver productos
templates = Jinja2Templates(directory="templates")
@app.get("/seeproducts", response_class=HTMLResponse)
async def read_item(request: Request,search:str=''):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"productsList": readAllProducts(search)}
    )

# ver carrito
templates = Jinja2Templates(directory="templates")
@app.get("/seecart/{userId}", response_class=HTMLResponse)
async def read_item(request: Request,userId:int):
    return templates.TemplateResponse(
        request=request, name="cart.html", context={"cartProducts": getCart(userId)}
    )
    


##########################################################

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
async def getProducts(search:str=''):   
    return readAllProducts(search)

@app.post("/product")
async def postProduct(productData: Product):
    print(f'producto creado: ', productData)
    return createProduct(productData)

@app.delete("/product/{id}")
async def getProducts(id:int):
    return deleteProduct(id)    
    
############# Carrito #################
@app.post("/cart")
async def addProductToCart(cartProduct: dict):
    # leemos los valores del body -> cartProduct
    print(f'producto agregado al carrito --> atributos: ', cartProduct)

    #agregamos lógica para que si amount es 0, no invoque upsertCartProduct sino a deleteCartProduct
    if(cartProduct['amount'] != 0):
        respuesta = upsertCartProduct(cartProduct['userId'],cartProduct['productId'],cartProduct['amount'])
    else:
        respuesta = deletCartProduct(cartProduct['userId'],cartProduct['productId'])
    return respuesta

@app.get("/cart/{userId}")
async def getCartByUserId(userId: int):
    carrito = getCart(userId)
    print(f'carrito del usuario "{userId}" --> ', carrito)
    # [
    #     {
    #         "id":1,
    #         "name":"",
    #         "description":"",
    #         "price":"",
    #         "img_url":"",
    #         "amount":0,
    #     }
    # ]
    return carrito


@app.delete("/cart")
async def deleteProductFromCart(cartProduct: dict):
    print(f'DELETE /cart  - producto eliminado del carrito --> atributos: ', cartProduct)

    # leemos los valores del body -> cartProduct
    respuesta = deletCartProduct(cartProduct['userId'],cartProduct['productId'])
    return respuesta