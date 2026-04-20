from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: int = Field(..., gt=0)
    stock: int = Field(..., gt=0)
    description: Optional[str]
@app.post("/products")
def product(product: Product):
    return f"{product.name} 상품이 성공적으로 등록 되었습니다."

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("products:app", host="0.0.0.0", port=8000)