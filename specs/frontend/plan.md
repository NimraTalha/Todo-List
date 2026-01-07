# Implementation Plan: Next.js Frontend

**Branch**: `phase2-web-frontend` | **Date**: 2026-01-06 | **Spec**: [specs/overview.md](../overview.md)

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Complete implementation of a Next.js 16+ frontend with TypeScript and Tailwind CSS for the Todo application. The frontend integrates Better Auth with JWT tokens for authentication, consumes REST API endpoints as defined in the specifications, and provides a responsive, accessible user interface for task management. The implementation follows Next.js App Router patterns with server components by default and client components where interactivity is required.

## Technical Context

**Language/Version**: TypeScript, Next.js 16+
**Primary Dependencies**: Next.js, React, Tailwind CSS, Better Auth, React Hook Form
**Storage**: Browser localStorage for JWT token storage
**Testing**: Manual testing (out of scope for this plan)
**Target Platform**: Web browsers (desktop and mobile)
**Project Type**: Web frontend
**Performance Goals**: Fast loading, responsive UI with smooth interactions
**Constraints**: Must work with existing backend API endpoints, secure JWT handling
**Scale/Scope**: Single-user focused with proper authentication and authorization

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

All frontend requirements align with the project constitution. The implementation follows security best practices for JWT handling and authentication flows.

## Project Structure

### Documentation (this feature)

```text
specs/frontend/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
frontend/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── navbar.tsx
│   ├── login/
│   │   └── page.tsx
│   ├── signup/
│   │   └── page.tsx
│   └── tasks/
│       ├── page.tsx
│       └── [id]/
│           ├── page.tsx
│           └── edit/
│               └── page.tsx
├── components/
│   ├── TaskItem.tsx
│   ├── TaskForm.tsx
│   └── TaskList.tsx
├── lib/
│   ├── api.ts
│   └── better-auth-client.ts
├── types/
│   └── task.ts
├── public/
├── styles/
├── package.json
├── next.config.js
├── tailwind.config.js
├── tsconfig.json
└── .env.example
```

**Structure Decision**: Option 2: Web application frontend with Next.js App Router structure. The existing frontend directory includes additional pages for individual task views and editing.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| JWT in localStorage | Simple client-side storage for auth tokens | Cookies would require more complex server-side setup |

## Implementation Phases

### Phase 1: Setup and Configuration
- Configure Next.js project with TypeScript and Tailwind CSS
- Set up Better Auth integration with JWT
- Configure environment variables for API base URL
- Set up project structure and basic routing

### Phase 2: Authentication System
- Implement login and signup pages
- Create protected route middleware/components
- Set up session management with Better Auth
- Implement logout functionality

### Phase 3: Core Task Management UI
- Implement task listing page with filtering and sorting
- Create task CRUD operations (Create, Read, Update, Delete)
- Implement task form with validation
- Add responsive design for all components

### Phase 4: API Integration and State Management
- Connect UI components to backend API endpoints
- Implement proper error handling and loading states
- Create centralized API client with JWT attachment
- Add optimistic updates where appropriate
- Implement individual task view and edit pages

### Phase 5: Polish and Accessibility
- Add loading states and error boundaries
- Implement responsive design improvements
- Add accessibility features (keyboard navigation, ARIA labels)
- Add proper form validation and user feedback

## Component Hierarchy Plan

```
Root Layout
├── Navbar (with auth state)
└── Page-specific content
    ├── Login Page
    ├── Signup Page
    └── Tasks Dashboard
        ├── TaskList (manages state)
        │   ├── Filter Controls
        │   ├── TaskForm (for create/edit)
        │   └── TaskItem (individual task)
        │       └── TaskEditForm (when editing)
        └── Task Creation Button
    └── Individual Task View
        └── Task Detail Page
            └── Task Edit Page
```

## Authentication Flow

1. User visits any page
2. If protected route and not authenticated → redirect to login
3. User enters credentials on login page
4. Better Auth handles authentication and returns JWT
5. JWT stored in localStorage
6. JWT attached to all API requests automatically
7. On logout, JWT removed and user redirected to login

## API Client Design

- Centralized `taskApi` object with methods for each endpoint:
  - GET /api/tasks - List all tasks for authenticated user
  - GET /api/tasks/{id} - Get single task
  - POST /api/tasks - Create a new task
  - PUT /api/tasks/{id} - Update task
  - DELETE /api/tasks/{id} - Delete task
  - PATCH /api/tasks/{id}/complete - Toggle completion status
- Base request function that automatically attaches JWT
- Error handling for unauthorized responses (401)
- Proper TypeScript typing for all requests and responses
- Query parameter support for filtering and sorting

## State Management Approach

- Client-side state management using React hooks (useState, useEffect)
- Better Auth for session state management
- Local state in components for form handling and UI interactions
- Minimal global state - most state kept component-local

## Responsiveness and Accessibility

- Mobile-first responsive design using Tailwind CSS
- Proper semantic HTML elements
- Keyboard navigation support
- ARIA labels for interactive elements
- Focus management for form elements
- Screen reader compatibility

## Risk Mitigation

1. **JWT Security**: Store tokens in localStorage (acknowledging XSS risks but implementing proper CSP)
2. **API Integration**: Thoroughly test all API endpoints before deployment
3. **Browser Compatibility**: Test on major browsers (Chrome, Firefox, Safari, Edge)
4. **Performance**: Implement proper loading states and error boundaries

## Key Features Implemented

- **User Authentication**: Complete login/signup flow with JWT token management
- **Task CRUD Operations**: Create, read, update, delete, and toggle completion status
- **Protected Routes**: Automatic redirect to login for unauthenticated users
- **Task Filtering**: Filter tasks by status (all, pending, completed)
- **Individual Task Views**: Dedicated pages for viewing and editing specific tasks
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Error Handling**: Proper error states and user feedback
- **Type Safety**: Full TypeScript integration with proper type definitions