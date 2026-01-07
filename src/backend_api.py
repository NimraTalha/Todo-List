"""
FastAPI Backend for Todo Application
This API connects the frontend to the existing Todo CLI application functionality.
"""
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime, date, timedelta
from pydantic import BaseModel
import sys
import os
import json
from passlib.context import CryptContext
import hashlib
import jwt
from datetime import datetime, timedelta

# Add the src directory to the path so we can import todo_app
sys.path.append(os.path.join(os.path.dirname(__file__)))

from todo_app import TodoList, Task as TodoTask

# JWT Configuration
SECRET_KEY = "dev-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="Todo API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Password hashing - using SHA256 with salt for simplicity (not production ready)
import secrets

def hash_password_sha256(password: str) -> str:
    """Simple SHA256 password hashing with salt for development"""
    salt = secrets.token_hex(16)  # 16 bytes = 32 hex chars
    pwdhash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return f"{pwdhash}:{salt}"

def verify_password_sha256(plain_password: str, hashed_password: str) -> bool:
    """Verify password against SHA256 hash"""
    pwdhash, salt = hashed_password.split(':')
    computed_hash = hashlib.sha256((plain_password + salt).encode('utf-8')).hexdigest()
    return computed_hash == pwdhash

# Pydantic models for API
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str

class User(BaseModel):
    id: str
    email: str
    name: str

class UserInDB(User):
    hashed_password: str

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

# In-memory storage for users (in production, use a database)
fake_users_db = {}

# In-memory todo list instance
todo_list = TodoList()

def verify_password(plain_password, hashed_password):
    return verify_password_sha256(plain_password, hashed_password)

def get_password_hash(password):
    return hash_password_sha256(password)

def get_user(email: str):
    if email in fake_users_db:
        user_dict = fake_users_db[email]
        return UserInDB(**user_dict)

def authenticate_user(email: str, password: str):
    user = get_user(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(request: Request):
    token_str = request.headers.get("Authorization")
    if not token_str or not token_str.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = token_str[7:]  # Remove "Bearer " prefix
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        token_data = TokenData(email=email)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_user(email=email)
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user

# Authentication endpoints
@app.post("/api/auth/signin")
async def login_user(user_credentials: UserLogin):
    user = authenticate_user(user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/api/auth/signup")
async def register_user(user_data: UserCreate):
    if user_data.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)
    user = UserInDB(
        id=str(len(fake_users_db) + 1),
        email=user_data.email,
        name=user_data.name,
        hashed_password=hashed_password
    )
    fake_users_db[user_data.email] = user.dict()

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/auth/session")
async def get_session(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/api/auth/signout")
async def logout_user():
    # For a stateless JWT system, we just instruct the frontend to remove the token
    return {"message": "Successfully logged out"}

@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

@app.get("/api/tasks")
def get_tasks():
    """Get all tasks"""
    tasks = []
    for task in todo_list.get_all_tasks():
        tasks.append({
            "id": task.id,
            "user_id": "default_user",  # For simplicity in this phase
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.created_at.isoformat()  # Using created_at as updated_at for simplicity
        })
    return tasks

@app.post("/api/tasks")
def create_task(task_data: TaskCreate):
    """Create a new task"""
    task = todo_list.add_task(task_data.title, task_data.description)
    # Mark as completed if specified
    if task_data.completed:
        todo_list.mark_task_complete(task.id, True)

    return {
        "id": task.id,
        "user_id": "default_user",
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at.isoformat(),
        "updated_at": task.created_at.isoformat()
    }

@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    """Get a specific task by ID"""
    task = todo_list.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task.id,
        "user_id": "default_user",
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at.isoformat(),
        "updated_at": task.created_at.isoformat()
    }

@app.put("/api/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    """Update a specific task"""
    existing_task = todo_list.get_task(task_id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Prepare update parameters
    title = task_data.title if task_data.title is not None else existing_task.title
    description = task_data.description if task_data.description is not None else existing_task.description

    # Update the task
    todo_list.update_task(
        task_id,
        title=title,
        description=description
    )

    # Update completion status if provided
    if task_data.completed is not None:
        todo_list.mark_task_complete(task_id, task_data.completed)

    updated_task = todo_list.get_task(task_id)
    return {
        "id": updated_task.id,
        "user_id": "default_user",
        "title": updated_task.title,
        "description": updated_task.description,
        "completed": updated_task.completed,
        "created_at": updated_task.created_at.isoformat(),
        "updated_at": updated_task.created_at.isoformat()  # In a full implementation, this would track actual updates
    }

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a specific task"""
    if not todo_list.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@app.patch("/api/tasks/{task_id}/complete")
def toggle_task_completion(task_id: int):
    """Toggle task completion status"""
    task = todo_list.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    new_status = not task.completed
    todo_list.mark_task_complete(task_id, new_status)

    updated_task = todo_list.get_task(task_id)
    return {
        "id": updated_task.id,
        "user_id": "default_user",
        "title": updated_task.title,
        "description": updated_task.description,
        "completed": updated_task.completed,
        "created_at": updated_task.created_at.isoformat(),
        "updated_at": updated_task.created_at.isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)