from typing import Annotated
from fastapi import FastAPI, Request, Response, Cookie, Depends
from validations import Ticket, Pasajero, Vuelo, Authentication

from typing import Optional

from . import models
# from .database import SessionLocal

# import db
# engine = create_engine('postgresql+psycopg2://bruno:cozxfdUSeluaSObPUUGMcdXm2o3mOeZZ@dpg-cq3il5aju9rs739fj7qg-a.oregon-postgres.render.com/test_iyxa')

# engine = create_engine('sqlite:///database.db')
# session = Session(engine)
# class Hero(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age: Optional[int] = None

# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# SQLModel.metadata.create_all(engine)

app = FastAPI()

listaTickets = [
    Ticket(id=1,
           pasajero = Pasajero(dni=123456654, nombre='Pepe', apellido='Argento', fecha_nacimiento=''),
           vuelo = Vuelo(origen='BRA', destino='ARG', fecha_partida='')),
    Ticket(id=2,
           pasajero = Pasajero(dni=123457878, nombre='Fulano', apellido='Mengano', fecha_nacimiento=''),
           vuelo = Vuelo(origen='ARG', destino='BRA', fecha_partida=''))           
]

credenciales = {
    # 'usuario': 'contraseña'
    'bruno@gmail.com': 'clave1234',
    'pepito123@gmail.com': 'contra4444',
}

def identificarUsuario(dataRequest:Cookie):
    # return dataRequest.cookies.get('loggedUser')
    return True
    

def pepe(input):
    print('pepe input-> ', input)
    return True

@app.post("/ticket")  # comprar vuelo
async def post_ticket(infoTicket:Ticket, req:Request, res:Response):
    print(f'la información del ticket es: {infoTicket}')

    # invocar una función que verifique de qué usuario proviene la request
    usuarioAutenticado = identificarUsuario(req)
    if(usuarioAutenticado != None):
        
        # db.session.add(hero_1)
        # db.session.commit()
        
        db_user = models.User(email='sdadas@ddd.com', hashed_password='sssssss')
        db.add(db_user)
        db.commit()
        db.refresh(db_user)


        # continuar con la compra
        listaTickets.append(infoTicket)
        return 'POST /ticket'
    else:
        # indicar que no se está autenticado.
        res.status_code = 400
        return 'Necesita autenticarse para completar la operación'
        


@app.get("/ticket/{id}")
async def get_ticket(id: int):
    print(f'Buscando ticket id={id}...')
    statement = db.select(db.Hero).where(db.Hero.name == "Deadpond")
    hero = db.session.exec(statement).first()
    print(hero)
    for t in listaTickets:
        if t.id == id: 
            return t
    return 'No se encontró el ticket buscado...'

@app.patch("/ticket/{id}")
async def patch_ticket(id: int, ticket:Ticket):
    global listaTickets
    print(f'Buscando ticket id={id}...')
    print('body: ', ticket)
    for t,index in listaTickets:
        if t.id == id: 
            t = ticket
            return f'Ticket actualizado: {t}'
    return 'No se encontró el ticket buscado...'

# método de autenticación
@app.post("/auth")
async def authenticate(body:Authentication, res:Response):
    """ request body:
        {
            "username":"bruno@gmail.com",
            "password":"....."
        }
    """    
    print(f'El usuario a autenticar es: {body.username}')
    print(f'Clave ingresada: {body.password}')

    if credenciales.get(body.username) == body.password:
        res.set_cookie('loggedUser', body.username )
        return f'Autenticación exitosa. Cookie -> loggedUser: {body.username}'
    else: 
        return 'Error de autenticación. Intente nuevamente.'





################# Cookies #################################################

@app.get("/set_cookie")
async def post_ticket(res:Response):    

    res.set_cookie('mi_cookie_2', 'pepitoooo')
    return 'Cookie generada!'


@app.get("/read_cookie")
async def post_ticket(miVariable: Request ):

    print(f'La cookie del usuario es: {miVariable.cookies}')
    return miVariable.cookies