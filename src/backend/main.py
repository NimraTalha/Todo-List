from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import tasks
from .routes import auth

# Create FastAPI app
app = FastAPI(title="Todo API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex=r"https?://localhost:300\d"  # Allow localhost:3000-3009
)

# Import and add JWT middleware
from .middleware.jwt import jwt_middleware
app.middleware("http")(jwt_middleware)

# Include routes
app.include_router(tasks.router, prefix="/api")
app.include_router(auth.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Create database tables on startup
from .models import User, Task
from sqlmodel import SQLModel
from .db import engine

@app.on_event("startup")
def on_startup():
    # Create database tables
    SQLModel.metadata.create_all(engine)