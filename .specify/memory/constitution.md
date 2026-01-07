<!--
Sync Impact Report:
- Version change: 1.1.0 → 2.0.0
- Modified principles: Updated to reflect Phase II Full-Stack Web Application requirements
- Added sections: Phase II Web Application Guidelines, Authentication Requirements, Database Schema, API Design Principles
- Removed sections: Phase I specific constraints
- Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated
- Follow-up TODOs: None
-->

# Project Constitution: Evolution of Todo App - Phase II

## Project Overview
This constitution defines the guiding principles, constraints, and AI interaction rules for building an evolving Todo application. The project has evolved from a simple in-memory CLI app in Phase I to a full-stack web application in Phase II with authentication. The project will continue to evolve to distributed cloud-native AI systems in Phase III. As Product Architects, we use spec-driven development to generate code via AI (Spec-Kit Plus integrated with Claude), focusing on high-level specs rather than boilerplate.

## Core Principles

### Spec-Driven Development
All features must originate from natural language or structured specs. AI interprets specs to produce code. Store all specs in /specs/ with organized structure by feature, API, database, and UI. No features should be invented or added beyond what is explicitly defined in the current spec. Each specification file serves as the single source of truth.

### Clean Code and Structure
Follow PEP 8 and modern web development standards. Use modular design: separate models for Task and User, API endpoints with proper routing, and clean UI components. No global variables; use type hints; handle errors gracefully. Code must be secure, efficient, and testable. Include comments for clarity. Avoid dependencies beyond essentials.

### No Manual Boilerplate
AI handles imports, setups, and repetitive code. Human input limited to specs and architecture. Every implementation must follow clean code principles: clarity, simplicity, single responsibility.

### Phased Evolution
Each phase builds on the previous one. Implement only the features defined for the current phase; Do not add future scalability, AI, or distributed concepts prematurely unless explicitly defined in current phase specs. Phase II includes full-stack web application with authentication and database persistence.

### Ethical and Quality Standards
Code must be secure, efficient, and testable. Include comments for clarity. Avoid dependencies beyond essentials. Use modern syntax appropriate for the tech stack. Implement proper security measures for web applications including authentication and authorization.

## Technology Constraints

Frontend: Next.js 16+, TypeScript, Tailwind CSS
Backend: FastAPI, SQLModel, Neon PostgreSQL
Authentication: Better Auth with JWT
Package Manager: UV or npm/pnpm as appropriate
AI Tools: Spec-Kit Plus for spec-to-code; Claude for prompt refinement or code synthesis if needed.
Environment: Cross-platform support (Linux, Windows WSL, macOS).
Database: Neon PostgreSQL with SQLModel ORM for Python backend.

## Phase II Web Application Guidelines

### Features to Implement
- Task CRUD operations (Create, Read, Update, Delete)
- User authentication (sign up, sign in, JWT token management)
- Task filtering and sorting
- Secure API endpoints that require authentication
- Responsive web UI with modern design

### Frontend Requirements
- Next.js 16+ with TypeScript
- Tailwind CSS for styling
- Proper state management for tasks and authentication
- JWT token handling for API requests
- Responsive design for various screen sizes

### Backend Requirements
- FastAPI with proper type hints
- SQLModel for database models and queries
- Better Auth for user management
- JWT token verification middleware
- Proper error handling and validation

### Authentication Requirements
- Use Better Auth with JWT plugin
- Shared BETTER_AUTH_SECRET environment variable
- Frontend attaches JWT to every API request
- Backend verifies JWT and enforces user ownership on all operations
- Return 401 Unauthorized on invalid/missing token
- User data isolation - users can only access their own tasks

### Database Schema
- Users table (managed by Better Auth): id, email, name, created_at
- Tasks table: id, user_id (foreign key), title, description, completed, created_at, updated_at
- Proper indexing on user_id and completed fields
- Foreign key relationships enforced

### API Design Principles
- RESTful endpoints following standard conventions
- JWT token in Authorization header: "Bearer <token>"
- Proper HTTP status codes (200, 201, 204, 401, 404, etc.)
- Input validation and sanitization
- Error responses with clear messages

## AI Prompting Rules

When generating code from specs: "Based on the following spec, generate clean, modern code for the Todo app Phase II. Adhere to the constitution's principles. Output only the code in appropriate directory structure."
For Claude Integration: Use Claude to refine specs if ambiguous: "Refine this spec for clarity, ensuring it covers edge cases and aligns with Phase II requirements."
Iteration: If code generation fails, revise spec and retry. Track in specs/ directory.
All implementations must be verified against the specification; Code generation must follow the latest spec in case of conflicts; Never merge multiple specs into one implementation.

## Repository Structure

constitution.md: This file.
.spec-kit/: Spec-Kit configuration files.
specs/: Specification files organized by type (features, api, database, ui).
specs/features/: Feature specifications (task-crud, authentication, chatbot).
specs/api/: API specifications (rest-endpoints, mcp-tools).
specs/database/: Database specifications (schema).
specs/ui/: UI specifications (components, pages).
specs/architecture.md: High-level architecture decisions.
src/: Source code for backend and frontend.
README.md: Setup instructions and project overview.
.gitignore: Standard ignores for Python and Node.js projects.

## Governance

This constitution overrides all other instructions; Amendments require documentation and approval; All implementations must verify compliance with this constitution; The latest spec takes precedence in case of conflicts.
This constitution governs Phase II implementation; amend for later phases.
Amendment procedure: Document reasoning and tradeoffs in history/adr/ directory.
Versioning policy: Follow semantic versioning (MAJOR.MINOR.PATCH).
Compliance review: Regular verification against principles during development.

**Version**: 2.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2026-01-06
