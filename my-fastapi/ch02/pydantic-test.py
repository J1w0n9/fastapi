from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None

class Product(BaseModel):
    name: str = Field(..., min_length=4, max_length=15)
    price: float = Field(..., gt=100.0, lt=1000000)
    stock: Optional[int] = 10

class AdminUser(User):
    role: str = "admin"

if __name__ == "__main__":
    u = User(id=1, name="Choi", age=26, email="")
    print(u)

    p = Product(name="blender", price=300000.0, stock=10)
    print(p)

    admin = AdminUser(id=2, name="ronk", age=23, email="")
    print(admin)