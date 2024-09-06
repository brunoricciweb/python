from fastapi import FastAPI, Request,Response,Form
from sqlmodel import Field, Session, SQLModel, create_engine, select, delete
from typing import Annotated

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from db import Product, create_db_and_tables, engine, readAllProducts, createProduct, deleteProduct,upsertCartProduct,getCart,deletCartProduct, authUser


app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


### Función para autenticar
def getAuthUserId(cookies):
    if 'cookieUserId' in cookies.keys(): 
        return cookies['cookieUserId']
    return False
###

################## Interfaz gráfica ######################
# login 
templates = Jinja2Templates(directory="templates")
@app.get("/login", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html", context={}
    )

# ver productos
templates = Jinja2Templates(directory="templates")
@app.get("/seeproducts", response_class=HTMLResponse)
async def read_item(request: Request,search:str=''):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"productsList": readAllProducts(search)}
    )

# ver carrito
templates = Jinja2Templates(directory="templates")
@app.get("/seecart", response_class=HTMLResponse)
async def read_item(request: Request, res:Response):

    userId = getAuthUserId(request.cookies)
    if userId == False:   # Si no está autenticado...
        res.status_code = 401  # seteamos status code de "no autorizado"
        return 'Error: no autorizado'
    
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
async def addProductToCart(cartProduct: dict, reqData:Request, res:Response):
    # reqData contiene todos los datos de la request (solicitud) del cliente
    # leemos los valores del body -> cartProduct
    print(f'producto agregado al carrito --> atributos: ', cartProduct)

    userId = getAuthUserId(reqData.cookies)
    if userId == False:   # Si no está autenticado...
        res.status_code = 401  # seteamos status code de "no autorizado"
        return 'Error: no autorizado'
    
    #agregamos lógica para que si amount es 0, no invoque upsertCartProduct sino a deleteCartProduct
    if(cartProduct['amount'] != 0):
        respuesta = upsertCartProduct(userId, cartProduct['productId'],cartProduct['amount'])
    else:
        respuesta = deletCartProduct(userId, cartProduct['productId'])
    return respuesta

@app.get("/cart")
async def getCartByUserId(reqData:Request, res:Response):

    userId = getAuthUserId(reqData.cookies)
    if userId == False:   # Si no está autenticado...
        res.status_code = 401  # seteamos status code de "no autorizado"
        return 'Error: no autorizado'

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
async def deleteProductFromCart(cartProduct: dict, reqData:Request, res:Response):
    print(f'DELETE /cart  - producto eliminado del carrito --> atributos: ', cartProduct)
    userId = getAuthUserId(reqData.cookies)
    if userId == False:   # Si no está autenticado...
        res.status_code = 401  # seteamos status code de "no autorizado"
        return 'Error: no autorizado'
    # leemos los valores del body -> cartProduct
    respuesta = deletCartProduct(userId,cartProduct['productId'])
    return respuesta


########## Autenticación ###########
@app.post("/login")
async def authlogin(email: Annotated[str, Form()], password: Annotated[str, Form()], res:Response):

    authenticatedUserId = authUser(email,password) 

    if authenticatedUserId != None:
        res.status_code = 200
        res.set_cookie('cookieUserId', authenticatedUserId)
        return 'Login exitoso!'
    
    res.status_code = 400
    return 'Credenciales inválidas. Reintente nuevamente.'

@app.get("/logout")
async def authlogout(res:Response):
    res.status_code = 200
    res.delete_cookie('cookieUserId')
    return 'Logout exitoso.'

#####################


################# Cookies #################################################
@app.get("/set_cookie/{userId}")
async def post_ticket(res:Response, userId:int=1):    
    res.set_cookie('cookieUserId', userId)
    return f'Cookie almacenada -> userId: {userId}'

@app.get("/read_cookie")
async def post_ticket(miVariable: Request ):
    print(f'Las cookies del usuario son: {miVariable.cookies}')

    userId = getAuthUserId(miVariable.cookies)
    print(f'usuario autenticado --> ', userId)

    return miVariable.cookies