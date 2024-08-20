from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select, delete

from db import Product, create_db_and_tables, engine, readAllProducts


app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
async def getProducts(search:str=''):   
    return readAllProducts(search)



@app.post("/product")
async def postProduct(productData: Product):

    print(f'producto creado: ', productData)
    with Session(engine) as session:
        session.add(productData)
        session.commit()
        session.refresh(productData)
        return productData
    


@app.delete("/product/{id}")
async def getProducts(id:int):
    with Session(engine) as session:
        product = session.exec(delete(Product).where(Product.id == id))
        session.commit()
        return product