from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ProductCreate(BaseModel):
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float

class ProductUpdate(BaseModel):
    quantity: int

class ProductOut(ProductCreate):
    id: Optional[str] = Field(None, alias="_id")
    class Config:
        orm_mode = True
        allow_population_by_field_name = True 