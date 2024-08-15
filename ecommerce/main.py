from fastapi import FastAPI

app = FastAPI()

productList = [{'name':'Teclado','price':15400.25,'img':'https://http2.mlstatic.com/D_NQ_NP_626103-MLA31936565669_082019-O.webp'}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
async def getProducts():
    return productList

@app.post("/product")
async def postProduct(productData: dict):

    print(f'producto creado: ', productData)
    productList.append(productData)

    return productData

