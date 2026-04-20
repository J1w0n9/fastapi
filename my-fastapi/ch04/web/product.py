import uvicorn
from fastapi import FastAPI

from ch04.database import product_repository
from ch04.model.product import Product

app = FastAPI()

@app.post("/items")
async def create_item(item: Product):
    result = product_repository.insert(item)
    return result


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)