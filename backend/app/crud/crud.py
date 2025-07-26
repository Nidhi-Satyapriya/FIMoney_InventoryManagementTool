from app.database.database import db
from app.models import model
from bson import ObjectId
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User CRUD

def get_user_by_username(username: str):
    return db.users.find_one({"username": username})

def create_user(user: model.User):
    user_dict = user.dict()
    # Do NOT hash the password here; it is already hashed in the route
    result = db.users.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user or not pwd_context.verify(password, user["password"]):
        return None
    return user

# Product CRUD

def create_product(product: model.Product):
    product_dict = product.dict()
    result = db.products.insert_one(product_dict)
    product_dict["_id"] = str(result.inserted_id)
    return product_dict

def update_product_quantity(product_id: str, quantity: int):
    result = db.products.update_one({"_id": ObjectId(product_id)}, {"$set": {"quantity": quantity}})
    if result.modified_count:
        prod = db.products.find_one({"_id": ObjectId(product_id)})
        prod["_id"] = str(prod["_id"])
        return prod
    return None

def get_products(skip: int = 0, limit: int = 10):
    products = list(db.products.find().skip(skip).limit(limit))
    for p in products:
        p["_id"] = str(p["_id"])
    return products

def get_total_products_count():
    """Get total number of products for pagination"""
    return db.products.count_documents({}) 