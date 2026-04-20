from typing import Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    price: int = Field(gt=0)
    stock: int = Field(gt=0)
    description: Optional[str] = None