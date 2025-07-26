from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    password: str
    role: UserRole = UserRole.USER

class Product(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float 