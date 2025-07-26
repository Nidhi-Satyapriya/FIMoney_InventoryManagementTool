from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Product(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float

class ProductCreate(BaseModel):
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float

class ProductOut(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float

class ProductUpdate(BaseModel):
    quantity: int

# Pagination schemas
class PaginationInfo(BaseModel):
    total: int
    page: int
    per_page: int
    total_pages: int
    has_next: bool
    has_prev: bool
    next_page: Optional[int] = None
    prev_page: Optional[int] = None

class ProductListResponse(BaseModel):
    products: List[ProductOut]
    pagination: PaginationInfo 