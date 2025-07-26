from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    password: str
    role: UserRole = UserRole.USER
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None

class Product(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

# Analytics Models
class ProductAnalytics(BaseModel):
    total_products: int
    total_value: float
    low_stock_products: int
    out_of_stock_products: int
    most_expensive_product: Optional[dict] = None
    least_expensive_product: Optional[dict] = None
    products_by_type: dict

class UserAnalytics(BaseModel):
    total_users: int
    active_users: int
    admin_users: int
    recent_registrations: List[dict]

class SystemAnalytics(BaseModel):
    total_products: int
    total_users: int
    total_value: float
    average_product_price: float
    top_product_types: List[dict]
    recent_activity: List[dict]

class AdminDashboard(BaseModel):
    product_analytics: ProductAnalytics
    user_analytics: UserAnalytics
    system_analytics: SystemAnalytics 