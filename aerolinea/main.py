from typing import Annotated
from fastapi import FastAPI, Request, Response, Cookie
from validations import Ticket, Pasajero, Vuelo, Authentication

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
    return dataRequest.cookies.get('loggedUser')
    

@app.post("/ticket")  # comprar vuelo
async def post_ticket(infoTicket:Ticket, req:Request, res:Response):
    print(f'la información del ticket es: {infoTicket}')

    # invocar una función que verifique de qué usuario proviene la request
    usuarioAutenticado = identificarUsuario(req)
    if(usuarioAutenticado != None):
        # continuar con la compra
        return 'POST /ticket'
    else:
        # indicar que no se está autenticado.
        res.status_code = 400
        return 'Necesita autenticarse para completar la operación'
        


@app.get("/ticket/{id}")
async def get_ticket(id: int):
    print(f'Buscando ticket id={id}...')
    for t in listaTickets:
        if t.id == id: return f'info ticket: {t}'
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





##################################################################

@app.get("/set_cookie")
async def post_ticket(res:Response):    

    res.set_cookie('mi_cookie_2', 'pepitoooo')
    return 'Cookie generada!'


@app.get("/read_cookie")
async def post_ticket(miVariable: Request ):

    print(f'La cookie del usuario es: {miVariable.cookies}')
    return miVariable.cookies