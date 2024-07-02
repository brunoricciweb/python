from pydantic import BaseModel
from enum import Enum

class Authentication(BaseModel):
    username: str
    password: str

class CodigoPais(Enum):
    AR = 'ARG'
    BR = 'BRA'
    aa = 123


class Pasajero(BaseModel):
    dni: int
    nombre: str
    apellido: str
    fecha_nacimiento: str

class Vuelo(BaseModel):
    destino: CodigoPais
    origen: CodigoPais
    fecha_partida: str

class Ticket(BaseModel):
    id: int | None = None
    pasajero: Pasajero
    vuelo: Vuelo