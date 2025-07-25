from fastapi import APIRouter, HTTPException, status
from app.schemas import schema
from app.crud import crud
from app.auth.auth import create_access_token, verify_password, get_password_hash

router = APIRouter()

@router.post("/register", response_model=schema.UserOut, status_code=201)
def register(user: schema.UserCreate):
    db_user = crud.get_user_by_username(user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="Username already registered")
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user_dict["password"])
    new_user = crud.create_user(schema.User(**user_dict))
    return schema.UserOut(**new_user)

@router.post("/login", response_model=schema.Token)
def login(user: schema.UserCreate):
    db_user = crud.get_user_by_username(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": db_user["username"]})
    return {"access_token": access_token, "token_type": "bearer"} 