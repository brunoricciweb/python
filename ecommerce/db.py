from sqlmodel import Field, Session, SQLModel, create_engine, select,delete



class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: float | None = Field(default=None, index=True)
    img_url: str = ''


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str

class Carts(SQLModel, table=True):
    id: int =  Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.id")
    product_id: int = Field(default=None, foreign_key="product.id")
    amount: int  # se envía en cada request de POST /cart


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
            products = session.exec(select(Product).where(Product.name.like(f'%{search}%'))).all()        
        return products

def createProduct(newProduct:Product):
    with Session(engine) as session:
        session.add(newProduct)
        session.commit()
        session.refresh(newProduct)
        return newProduct

def deleteProduct(id:int):
    with Session(engine) as session:
        product = session.exec(delete(Product).where(Product.id == id))
        session.commit()
        return product

def getCart(userId):
    with Session(engine) as session:
        cart = session.exec(  select(Carts,Product).where(Carts.product_id == Product.id).where(Carts.user_id == userId)  )
        print('****************************')
        cartProducts = []
        for c, p in cart:
            auxProduct = dict(p)
            auxProduct['amount'] = c.amount
            cartProducts.append(auxProduct)
            print(' auxProduct ---> ', auxProduct)
        return cartProducts

def setCartProduct(userId, productId, amount):
    # userId -> id del usuario
    # productId -> id del producto
    # amount -> cantidad de unidades de producto
    nuevoRegistro = Carts(user_id=userId,product_id=productId,amount=amount)

    ###BUG
    # leer tabla Carts. Si el product_id existe, pisar/actualizar ese mismo registo.
    # si el product_id NO existe, insertar directamente

    with Session(engine) as session:
        session.add(nuevoRegistro)
        session.commit()
        session.refresh(nuevoRegistro)
        return nuevoRegistro