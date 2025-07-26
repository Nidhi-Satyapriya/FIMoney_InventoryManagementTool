from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, products
import os

# Initializing FastAPI app 
app = FastAPI(
    title="FIMoney Inventory Management Tool API",
    description="A comprehensive inventory management system API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS for production
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# user and product routers
app.include_router(users.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(products.router, prefix="/api/v1", tags=["Products"])

@app.get("/")
def read_root():
    """Root endpoint - API health check"""
    return {
        "message": "Welcome to the FIMoney Inventory Management Tool API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"} 