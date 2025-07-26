from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.model import UserRole

# User Schemas
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    role: UserRole = UserRole.USER

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    role: UserRole
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None

class Token(BaseModel):
    access_token: str
    token_type: str
    user_role: UserRole

# Product Schemas
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: str = Field(..., min_length=1, max_length=50)
    sku: str = Field(..., min_length=1, max_length=50)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., gt=0)
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    type: Optional[str] = Field(None, min_length=1, max_length=50)
    sku: Optional[str] = Field(None, min_length=1, max_length=50)
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProductQuantityUpdate(BaseModel):
    quantity: int = Field(..., ge=0)

class ProductResponse(BaseModel):
    id: str
    name: str
    type: str
    sku: str
    quantity: int
    price: float
    description: Optional[str] = None
    image_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

# Pagination Schema
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
    products: List[ProductResponse]
    pagination: PaginationInfo

# Admin Schemas
class AdminUserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    role: UserRole = UserRole.ADMIN

class AdminUserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    role: Optional[UserRole] = None

class AdminDashboardResponse(BaseModel):
    product_analytics: dict
    user_analytics: dict
    system_analytics: dict
    recent_activity: List[dict]

class AnalyticsFilter(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    product_type: Optional[str] = None
    user_role: Optional[UserRole] = None

# Response Messages
class MessageResponse(BaseModel):
    message: str

class ProductCreateResponse(BaseModel):
    product_id: str
    message: str 