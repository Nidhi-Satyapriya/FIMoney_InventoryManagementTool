from fastapi import FastAPI
from app.routes import users, products

app = FastAPI(title="Inventory Management Tool API")

# Include user and product routers
app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory Management Tool API"} 