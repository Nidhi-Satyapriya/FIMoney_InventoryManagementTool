from fastapi import APIRouter, HTTPException, status
from app.schemas import schema
from app.crud import crud
from app.auth.auth import create_access_token, verify_password, get_password_hash
from app.models import model

router = APIRouter()

@router.post("/register", response_model=schema.UserOut, status_code=201)
def register(user: schema.UserCreate):
    """Register a new user"""
    # Check if user already exists
    db_user = crud.get_user_by_username(user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Username already registered"
        )
    
    # Hash password and create user
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user_dict["password"])
    new_user = crud.create_user(model.User(**user_dict))
    
    return schema.UserOut(**new_user)

@router.post("/login", response_model=schema.Token)
def login(user: schema.UserCreate):
    """Authenticate user and return JWT token"""
    # Verify user credentials
    db_user = crud.get_user_by_username(user.username)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="User not found"
        )
    
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect password"
        )
    
    # Generate access token
    access_token = create_access_token(data={"sub": db_user["username"]})
    return {"access_token": access_token, "token_type": "bearer"} 