from fastapi import FastAPI
from validations import Ticket, Pasajero, Vuelo

app = FastAPI()

listaTickets = [
    Ticket(id=1,
           pasajero = Pasajero(dni=123456654, nombre='Pepe', apellido='Argento', fecha_nacimiento=''),
           vuelo = Vuelo(origen='BRA', destino='ARG', fecha_partida='')),
    Ticket(id=2,
           pasajero = Pasajero(dni=123457878, nombre='Fulano', apellido='Mengano', fecha_nacimiento=''),
           vuelo = Vuelo(origen='ARG', destino='BRA', fecha_partida=''))           
]

@app.post("/ticket")
async def post_ticket(infoTicket:Ticket):
    print(f'la información del ticket es: {infoTicket}')
    return 'POST /ticket'


@app.get("/ticket/{id}")
async def get_ticket(id: int):
    print(f'Buscando ticket id={id}...')
    for t in listaTickets:
        if t.id == id: return f'info ticket: {t}'
    return 'No se encontró el ticket buscado...'

