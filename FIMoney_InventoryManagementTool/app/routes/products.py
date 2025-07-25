from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas import schema
from app.crud import crud
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.post("/products", response_model=dict, status_code=201)
def add_product(product: schema.ProductCreate, user=Depends(get_current_user)):
    db_product = crud.create_product(product)
    return {"product_id": db_product["_id"], "message": "Product added successfully"}

@router.put("/products/{id}/quantity", response_model=schema.ProductOut)
def update_quantity(id: str, payload: schema.ProductUpdate, user=Depends(get_current_user)):
    updated_product = crud.update_product_quantity(id, payload.quantity)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.get("/products", response_model=List[schema.ProductOut])
def get_products(skip: int = 0, limit: int = 10, user=Depends(get_current_user)):
    products = crud.get_products(skip=skip, limit=limit)
    return products 