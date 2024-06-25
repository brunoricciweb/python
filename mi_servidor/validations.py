from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    categoria: str  | None = None
    precio: float