---
name: task-crud-operations
description: Create, list, update, complete, and delete Todo tasks following project specs. Use whenever implementing or modifying task management features.
---

# Task CRUD Operations

## Instructions
Follow these steps exactly when handling task operations:

1. Always reference /specs/features/task-crud.md and /specs/api/rest-endpoints.md
2. For create task:
   - Require title (1-200 chars)
   - Optional description (max 1000 chars)
   - Associate with authenticated user_id
3. For list tasks:
   - Show only tasks belonging to current user
   - Display title, status, created date
   - Support filtering by status (all/pending/completed)
4. For update/delete/complete:
   - Verify task belongs to current user
   - Use correct REST endpoint
5. Implement using proper frontend components and backend routes
6. Add clear success/error messages in UI

## Examples

**Create Task Example (Backend Route)**
```python
# In routes/tasks.py
@router.post("/")
async def create_task(task: TaskCreate, current_user: User = Depends(get_current_user)):
    new_task = Task(title=task.title, description=task.description, user_id=current_user.id)
    db.add(new_task)
    await db.commit()
    return new_task