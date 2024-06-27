from fastapi import FastAPI
from validations import Ticket

app = FastAPI()

@app.post("/ticket")
async def post_ticket(infoTicket:Ticket):
    print(f'la información del ticket es: {infoTicket}')
    return 'POST /ticket'