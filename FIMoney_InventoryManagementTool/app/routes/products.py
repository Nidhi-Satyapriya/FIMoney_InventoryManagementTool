from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas import schema
from app.crud import crud
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.post("/products", response_model=dict, status_code=201)
def add_product(product: schema.ProductCreate, user=Depends(get_current_user)):
    """Add a new product to inventory"""
    try:
        db_product = crud.create_product(product)
        return {
            "product_id": db_product["_id"], 
            "message": "Product added successfully"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create product"
        )

@router.put("/products/{id}/quantity", response_model=schema.ProductOut)
def update_quantity(id: str, payload: schema.ProductUpdate, user=Depends(get_current_user)):
    """Update product quantity"""
    try:
        updated_product = crud.update_product_quantity(id, payload.quantity)
        if not updated_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Product not found"
            )
        return updated_product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update product quantity"
        )

@router.get("/products", response_model=List[schema.ProductOut])
def get_products(skip: int = 0, limit: int = 10, user=Depends(get_current_user)):
    """Get list of products with pagination"""
    try:
        products = crud.get_products(skip=skip, limit=limit)
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve products"
        ) 