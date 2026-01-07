# Tasks: Full Stack Todo App - Phase 2 Backend Implementation

## Feature Overview
Complete FastAPI backend with Neon PostgreSQL integration for the existing CLI Todo app. Implementation includes JWT authentication with Better Auth, SQLModel ORM, and secure API endpoints for full frontend integration.

## Implementation Strategy
- Complete backend infrastructure with database models
- JWT authentication middleware with Better Auth integration
- Secure API endpoints with user isolation
- Environment configuration for production readiness
- Full integration testing with frontend

## Dependencies
- Backend implementation depends on existing CLI functionality
- Database schema implementation precedes API routes
- Authentication middleware implementation precedes route protection

---

## Phase 1: Backend Infrastructure Setup

- [x] T001 Create project structure: `src/backend/{models,routes,middleware}`
- [x] T002 Set up development environment with required dependencies
- [x] T003 Verify existing CLI functionality works before backend changes

---

## Phase 2: Database Layer Implementation

- [x] T004 Implement SQLModel models for User and Task entities in `src/backend/models.py`
- [x] T005 Add proper relationships, constraints, and indexes as per schema spec
- [x] T006 Set up database connection with Neon PostgreSQL in `src/backend/db.py`
- [x] T007 Implement session management with proper connection pooling

**Story Goal**: Create robust database layer with proper relationships and indexing.

**Independent Test Criteria**:
- User model with id, email, name, created_at fields
- Task model with id, user_id, title, description, completed, created_at, updated_at
- Foreign key relationship between Task.user_id and User.id
- Indexes on user_id and completed fields for performance

---

## Phase 3: Authentication Layer

- [x] T008 Implement JWT verification middleware in `src/backend/middleware/jwt.py`
- [x] T009 Extract and validate tokens from Authorization: Bearer header
- [x] T010 Verify tokens using shared BETTER_AUTH_SECRET from .env
- [x] T011 Enforce user_id matching and return 401 on invalid tokens

**Story Goal**: Secure backend with JWT authentication using Better Auth integration.

**Independent Test Criteria**:
- Middleware intercepts all requests and validates JWT tokens
- Proper extraction of user_id from JWT payload
- 401 Unauthorized responses for invalid/missing tokens
- Stateless authentication without sessions

---

## Phase 4: API Endpoints Implementation

- [x] T012 Implement GET /api/tasks endpoint with query params (status, sort)
- [x] T013 Implement POST /api/tasks endpoint for task creation
- [x] T014 Implement GET /api/tasks/{id} endpoint for single task retrieval
- [x] T015 Implement PUT /api/tasks/{id} endpoint for task updates
- [x] T016 Implement DELETE /api/tasks/{id} endpoint for task deletion
- [x] T017 Implement PATCH /api/tasks/{id}/complete endpoint for toggling completion
- [x] T018 Add user isolation - verify user_id matches JWT for all operations

**Story Goal**: Complete task CRUD operations with proper authentication and user isolation.

**Independent Test Criteria**:
- All endpoints require valid JWT in Authorization header
- GET /api/tasks supports status and sort query parameters
- User isolation enforced - users can only access their own tasks
- Proper error handling with HTTPException responses

---

## Phase 5: Application Setup

- [x] T019 Create main FastAPI application in `src/backend/main.py`
- [x] T020 Configure CORS middleware for frontend origin (http://localhost:3000)
- [x] T021 Include task routes with proper prefix
- [x] T022 Add JWT middleware to application

**Story Goal**: Complete FastAPI application with proper configuration.

**Independent Test Criteria**:
- CORS configured for frontend origin
- All routes properly included with /api prefix
- JWT middleware applied to all routes
- Health and root endpoints available

---

## Phase 6: Environment and Dependencies

- [x] T023 Create .env file with BETTER_AUTH_SECRET, DATABASE_URL, NEXTAUTH_URL
- [x] T024 Update requirements.txt with all necessary dependencies
- [x] T025 Create main.py entry point for running the server
- [x] T026 Add automatic database table creation on startup

**Story Goal**: Proper environment configuration for secure deployment.

**Independent Test Criteria**:
- Environment variables properly loaded with python-dotenv
- All required dependencies in requirements.txt
- Server runs on port 8000 and accessible to frontend
- Database tables created automatically on startup

---

## Phase 7: Integration & Testing

- [x] T027 Test all backend modules can be imported successfully
- [x] T028 Verify environment variables are properly loaded
- [x] T029 Test API endpoints are accessible
- [x] T030 Verify integration readiness with frontend at http://localhost:3000

**Story Goal**: Complete backend implementation ready for frontend integration.

**Independent Test Criteria**:
- All modules import without errors
- Environment variables loaded correctly
- API endpoints accessible with proper authentication
- Backend ready for full stack integration

---

## Phase 8: Documentation & Polish

- [x] T031 Update README.md with backend implementation details
- [x] T032 Document API endpoints and usage instructions
- [x] T033 Create backend implementation summary
- [x] T034 Final code review and cleanup

**Story Goal**: Complete documentation for backend implementation.

**Independent Test Criteria**:
- README updated with backend architecture
- API endpoints documented with authentication requirements
- Setup instructions clear for frontend integration
- Code follows established patterns and standards