<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: All principles updated to reflect comprehensive requirements
- Added sections: Technology Constraints, Phase I Specifications Guidelines, AI Prompting Rules, Repository Structure
- Removed sections: N/A
- Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated
- Follow-up TODOs: None
-->

# Project Constitution: Evolution of Todo App

## Project Overview
This constitution defines the guiding principles, constraints, and AI interaction rules for building an evolving Todo application. The project starts with a simple in-memory CLI app in Phase I and progresses to distributed cloud-native AI systems. As Product Architects, we use spec-driven development to generate code via AI (Spec-Kit Plus integrated with Qwen), focusing on high-level specs rather than boilerplate.

## Core Principles

### Spec-Driven Development
All features must originate from natural language or structured specs. AI interprets specs to produce Python code. Store all specs in /specs-history/ with versioned filenames (e.g., v1_add_task.spec.yaml). No features should be invented or added beyond what is explicitly defined in the current spec. Each specification file serves as the single source of truth.

### Clean Code and Structure
Follow PEP 8. Use modular design: separate classes for Task (with id, title, description, completed bool), TodoList (managing tasks), and CLI interface. No global variables; use type hints; handle errors gracefully. Code must be secure, efficient, and testable. Include comments for clarity. Avoid dependencies beyond essentials.

### No Manual Boilerplate
AI handles imports, setups, and repetitive code. Human input limited to specs and architecture. Every implementation must follow clean code principles: clarity, simplicity, single responsibility.

### Phased Evolution
Phase I is in-memory only. Design for extensibility (e.g., abstract storage interface for future persistence). Implement only the features defined for the current phase; Do not add future scalability, cloud, AI, or distributed concepts prematurely; Phase I is limited to in-memory CLI application.

### Ethical and Quality Standards
Code must be secure, efficient, and testable. Include comments for clarity. Avoid dependencies beyond essentials. Use Python 3.13+ syntax; Avoid unnecessary abstractions or frameworks in early phases.

## Technology Constraints

Language: Python 3.13+
Package Manager: UV (for fast installs; e.g., uv venv, uv pip install)
AI Tools: Spec-Kit Plus for spec-to-code; Qwen for prompt refinement or code synthesis if needed.
Environment: Linux-based (use WSL 2 with Ubuntu 22.04 on Windows).
No External Dependencies for Phase I: Core Python only (e.g., no databases, use lists/dicts for storage).

## Phase I Specifications Guidelines

Features: Implement exactly: Add task (title, desc), Delete by ID, Update by ID, View all with status ([ ] incomplete, [x] complete), Mark complete/incomplete by ID.
CLI Interface: Interactive loop with commands (e.g., 'add <title> <desc>', 'list', 'update <id> <new_title> <new_desc>', etc.). Use input() or argparse for parsing.
Data Model: Tasks have auto-incrementing IDs starting from 1. In-memory storage (list of dicts or Task objects).
Validation: Check for invalid IDs, empty inputs; provide user-friendly messages.
Exit: Command like 'quit' to end the app.
Use in-memory data structures only (e.g., list of dictionaries); No databases, files, or persistent storage in Phase I; Todos exist only during program runtime.

## AI Prompting Rules

When generating code from specs: "Based on the following spec, generate clean Python 3.13 code for the Todo app. Adhere to the constitution's principles. Output only the code in /src/ structure."
For Qwen Integration: Use Qwen to refine specs if ambiguous: "Refine this spec for clarity, ensuring it covers edge cases and aligns with Phase I requirements."
Iteration: If code generation fails, revise spec and retry. Track in specs-history.
All implementations must be verified against the specification; Code generation must follow the latest spec in case of conflicts; Never merge multiple specs into one implementation.

## Repository Structure

constitution.md: This file.
specs-history/: Versioned spec files.
src/: Python code (e.g., main.py, models.py, cli.py).
README.md: Setup (WSL install, uv setup, run instructions), demo commands.
.gitignore: Standard Python ignores.

## Governance

This constitution overrides all other instructions; Amendments require documentation and approval; All implementations must verify compliance with this constitution; The latest spec takes precedence in case of conflicts.
This constitution is immutable for Phase I; amend for later phases.
Amendment procedure: Document reasoning and tradeoffs in history/adr/ directory.
Versioning policy: Follow semantic versioning (MAJOR.MINOR.PATCH).
Compliance review: Regular verification against principles during development.

**Version**: 1.1.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-12-27
