# REST API Endpoints

## Base URL
- Development: http://localhost:8000

## Authentication
All endpoints require JWT token in header:
Authorization: Bearer <token>

## Endpoints (note: routes simplified to /api/tasks without user_id in path - user extracted from JWT)

### GET /api/tasks
List all tasks for authenticated user.

Query Parameters:
- status: "all" | "pending" | "completed"
- sort: "created" | "title"

### POST /api/tasks
Create a new task (title required, description optional)

### GET /api/tasks/{id}
Get single task (must belong to user)

### PUT /api/tasks/{id}
Update task

### DELETE /api/tasks/{id}
Delete task

### PATCH /api/tasks/{id}/complete
Toggle completion status