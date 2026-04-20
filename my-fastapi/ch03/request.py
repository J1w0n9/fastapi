from typing import Optional

import fastapi
from pydantic import BaseModel, Field


app = fastapi.FastAPI()
fake_items_db = [{"item_name": "notebook"}, {"item_name": "phone"}, {"item_name": "pad"}]
products = []

class Product(BaseModel):
    name: str = Field(min_length=2)
    price: int = Field(gt=0)
    tax: float | None = None
    stock: int = Field(gt=0)
    description: Optional[str] = None
    is_sale: bool = False

@app.get("/items/all")
async def read_all_items():
    return {"message": "all items"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items")
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip: skip + limit]

@app.get("/items_pq/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items_nd/")
async def read_item_nd(skip: int, limit: int):
    return fake_items_db[skip : skip + limit]

@app.get("/items_pq/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items_tax")
def create_item_tax(item: Product):
    item_dic = item.model_dump()
    print(item_dic)
    if item.tax:
        price_with_tax = item.price + item.price * item.tax
        item_dic.update({"price": price_with_tax})
    return item_dic

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Product, q: str | None = None, discount: float = 0.0 ):
    result = {
        "item_id": item_id,
        "item": item.model_dump(),
        "discount": discount
    }
    if q:
        result["q"] = q
    return result



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("request:app", host="0.0.0.0", port=8000)