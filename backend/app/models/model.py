from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    password: str

class Product(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float 