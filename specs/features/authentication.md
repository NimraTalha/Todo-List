# Feature: User Authentication

## User Stories
- As a user, I can sign up with email and password
- As a user, I can sign in with email and password
- As a user, I can access my tasks only after login
- As a user, my data is isolated from other users

## Acceptance Criteria
- Use Better Auth with JWT plugin
- Shared BETTER_AUTH_SECRET environment variable
- Frontend attaches JWT to every API request
- Backend verifies JWT and enforces user ownership on all operations
- Return 401 Unauthorized on invalid/missing token