from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlmodel import Session, select, and_
from typing import List, Optional
from datetime import datetime

from ..db import get_session
from ..models import Task, TaskCreate, TaskUpdate, TaskRead

router = APIRouter()

@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(
    request: Request,
    status: Optional[str] = Query(None, description="Filter by status: all, pending, completed"),
    sort: Optional[str] = Query(None, description="Sort by: created, title"),
    session: Session = Depends(get_session)
):
    # Get user_id from request state (set by JWT middleware)
    user_id = request.state.user_id

    # Build query with user_id filter
    query = select(Task).where(Task.user_id == user_id)

    # Apply status filter
    if status and status != "all":
        if status == "pending":
            query = query.where(Task.completed == False)
        elif status == "completed":
            query = query.where(Task.completed == True)

    # Apply sorting
    if sort == "title":
        query = query.order_by(Task.title)
    else:  # Default or "created"
        query = query.order_by(Task.created_at.desc())

    tasks = session.exec(query).all()
    return tasks


@router.post("/tasks", response_model=TaskRead)
def create_task(
    request: Request,
    task_data: TaskCreate,
    session: Session = Depends(get_session)
):
    # Get user_id from request state (set by JWT middleware)
    user_id = request.state.user_id

    # Verify that the user_id in the request matches the one in the JWT
    # (This is a security measure to ensure users can't create tasks for other users)
    task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        user_id=user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(
    request: Request,
    task_id: int,
    session: Session = Depends(get_session)
):
    # Get user_id from request state (set by JWT middleware)
    user_id = request.state.user_id

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the authenticated user
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this task")

    return task


@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(
    request: Request,
    task_id: int,
    task_data: TaskUpdate,
    session: Session = Depends(get_session)
):
    # Get user_id from request state (set by JWT middleware)
    user_id = request.state.user_id

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the authenticated user
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    # Update task fields
    update_data = task_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    # Update the updated_at timestamp
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.delete("/tasks/{task_id}")
def delete_task(
    request: Request,
    task_id: int,
    session: Session = Depends(get_session)
):
    # Get user_id from request state (set by JWT middleware)
    user_id = request.state.user_id

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the authenticated user
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")

    session.delete(task)
    session.commit()

    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete")
def toggle_task_completion(
    request: Request,
    task_id: int,
    session: Session = Depends(get_session)
):
    # Get user_id from request state (set by JWT middleware)
    user_id = request.state.user_id

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the authenticated user
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    # Toggle completion status
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)

    return {"id": task.id, "completed": task.completed}