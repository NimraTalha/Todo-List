from sqlmodel import SQLModel, Field, create_engine, Index
from typing import Optional
from datetime import datetime
import uuid

# User model (managed by Better Auth, but we need it for FK)
class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False, max_length=255)
    name: str = Field(max_length=255)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class User(UserBase, table=True):
    __tablename__ = "users"

    # Define indexes
    __table_args__ = (
        Index("idx_users_email", "email"),  # Index on email
    )

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    # Hashed password field for authentication
    hashed_password: Optional[str] = Field(default=None, max_length=255, nullable=True)
    # Note: Better Auth manages user creation on frontend,
    # but backend needs the table for FK relationships

# Task model
class TaskBase(SQLModel):
    title: str = Field(nullable=False, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str = Field(foreign_key="users.id", index=True)  # Index on user_id as per spec
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Task(TaskBase, table=True):
    __tablename__ = "tasks"

    # Define indexes as per spec
    __table_args__ = (
        Index("idx_tasks_user_id", "user_id"),      # Index on user_id
        Index("idx_tasks_completed", "completed"),  # Index on completed
    )

    id: Optional[int] = Field(default=None, primary_key=True)

# Pydantic models for API requests/responses
from pydantic import BaseModel

class TaskCreate(TaskBase):
    title: str
    description: Optional[str] = None

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskRead(TaskBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime

class UserRead(UserBase):
    id: str

class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: str
    email: str