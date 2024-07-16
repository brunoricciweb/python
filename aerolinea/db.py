from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine('sqlite:///database.db')
session = Session(engine)

SQLModel.metadata.create_all(engine)

# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")