from sqlmodel import Field, Session, SQLModel, create_engine, select



class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: float | None = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def readAllProducts(search:str):
    with Session(engine) as session:
        products = []
        if(search != None):
            products = session.exec(select(Product)).all()
        if(search != ''):
            products = session.exec(select(Product).where(Product.name.like('%'+search+'%'))).all()        
        return products

def createProduct(newProduct:Product):

    pass