# Todo App Frontend

A Next.js frontend for the Todo application with authentication and task management.

## Features

- User authentication (login/signup)
- Task CRUD operations
- Task filtering (all/pending/completed)
- Responsive design with Tailwind CSS
- JWT-based authentication with Better Auth

## Tech Stack

- Next.js 14
- TypeScript
- Tailwind CSS
- Better Auth (for authentication)

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Create a `.env.local` file with your environment variables:
```bash
cp .env.example .env.local
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## API Integration

The frontend connects to the backend API at `http://localhost:8000` and uses JWT tokens for authentication. All API requests include the Authorization header with the stored JWT token.

## Project Structure

```
frontend/
├── app/                 # Next.js app router pages
│   ├── login/           # Login page
│   ├── signup/          # Signup page
│   ├── tasks/           # Tasks dashboard
│   └── layout.tsx       # Root layout
├── components/          # Reusable UI components
├── lib/                 # API client and utilities
├── types/               # TypeScript type definitions
└── utils/               # Helper functions
```