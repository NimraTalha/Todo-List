# Todo Application - Full Stack Implementation

A complete full-stack todo application with CLI, web frontend, and FastAPI backend integrated with Neon PostgreSQL.

## Features

1. **CLI Application** – Interactive command-line interface with advanced task management
2. **Web Frontend** – Modern Next.js interface for task management
3. **FastAPI Backend** – Robust API with Neon PostgreSQL integration
4. **User Authentication** – JWT-based authentication with Better Auth
5. **Task CRUD Operations** – Complete task management with filtering and sorting
6. **Data Persistence** – Secure database storage with user isolation

## Project Phases

### Phase I: CLI Application
- In-memory todo application with basic CRUD operations
- Advanced features: due dates, priorities, tags, recurrence, search, notifications

### Phase II: Full-Stack Web Application
- **Backend**: FastAPI with SQLModel and Neon PostgreSQL
- **Frontend**: Next.js 16+ with TypeScript and Tailwind CSS
- **Authentication**: Better Auth with JWT
- **API Integration**: Secure REST API endpoints with user isolation

## Backend Implementation

### Features Implemented

- **Task CRUD Operations**: Create, read, update, delete, and toggle completion status for tasks
- **User Authentication**: JWT-based authentication with Better Auth integration
- **Database Integration**: Neon Serverless PostgreSQL with SQLModel ORM
- **User Isolation**: Each user can only access their own tasks
- **API Endpoints**: RESTful API with proper error handling

### Database Schema

- **users** table:
  - `id` (string, primary key)
  - `email` (string, unique)
  - `name` (string)
  - `created_at` (timestamp)

- **tasks** table:
  - `id` (integer, primary key)
  - `user_id` (string, foreign key -> users.id)
  - `title` (string, not null)
  - `description` (text, nullable)
  - `completed` (boolean, default false)
  - `created_at` (timestamp)
  - `updated_at` (timestamp)

### API Endpoints

All endpoints require JWT token in header: `Authorization: Bearer <token>`

- `GET /api/tasks` - List all tasks for authenticated user
  - Query Parameters: `status` ("all"|"pending"|"completed"), `sort` ("created"|"title")
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get single task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
- `PATCH /api/tasks/{id}/complete` - Toggle completion status

### Running the Backend

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env` file:
   ```env
   BETTER_AUTH_SECRET=your_shared_secret_here
   DATABASE_URL=postgresql://user:pass@neon-host:5432/db_name
   NEXTAUTH_URL=http://localhost:3000
   ```

3. Run the server:
   ```bash
   python main.py
   ```

The backend will be available at `http://localhost:8000`

### Frontend Integration

The backend is designed to work seamlessly with the frontend running at `http://localhost:3000`, with proper CORS configuration and JWT authentication flow.

## CLI Application Usage

When you run the CLI application, you'll enter an interactive loop. Available commands:

- `add` - Add a new task (with optional due date, priority, tags, recurrence, and due datetime)
- `delete` - Delete a task by ID
- `update` - Update a task by ID (with optional due date, priority, tags, recurrence, and due datetime)
- `list` or `ls` - View all tasks (with optional filtering and sorting)
- `search` - Search tasks by keyword
- `remind` - Show reminder for a specific task with browser notification
- `complete` - Mark a task as complete (auto-generates new recurring tasks if applicable)
- `incomplete` - Mark a task as incomplete
- `quit` or `exit` - Exit the application

## Project Structure

- `src/backend/` - FastAPI backend implementation
- `src/todo_app.py` - CLI application code
- `test_todo_app.py` - Unit tests for all features
- `specs/` - Specification files
- `README.md` - This file

## Development

### Running Tests

```bash
python -m unittest test_todo_app.py -v
```

### Code Standards

- PEP 8 compliant
- Full type hints
- Comprehensive docstrings
- Defensive programming practices
- User-friendly messages