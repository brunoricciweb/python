from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

from db import Product, create_db_and_tables, engine

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/product")
def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


@app.get("/products")
def read_products():
    with Session(engine) as session:
        heroes = session.exec(select(Product)).all()
        return heroes