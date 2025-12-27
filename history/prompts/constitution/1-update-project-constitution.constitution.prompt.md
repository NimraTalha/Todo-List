---
id: 1
title: Update project constitution
stage: constitution
date: 2025-12-27
surface: agent
model: gpt-4o
feature: none
branch: main
user: jc
command: /sp.constitution
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution ### Project Analysis

#### Overview
The project, titled "The Evolution of Todo," is designed as a hackathon-style exercise to simulate the real-world progression of software development. It emphasizes spec-driven development, where AI (specifically modeled as Qwen) acts as a software engineer to generate code strictly based on provided specifications. The core theme is evolving a simple todo application from a basic command-line interface (CLI) to a sophisticated, distributed, cloud-native, AI-integrated system. This evolution happens in phases, starting with Phase I, which is the current focus as per the instructions.

The goal is for participants (students or developers) to act as "Product Architects." They define specifications, and the AI implements them without adding unsolicited features, boilerplate, or advanced concepts prematurely. This promotes clean, iterative development while avoiding over-engineering. The project explicitly prohibits inventing features, using persistent storage early on, or incorporating frameworks/distributed systems until later phases.

#### Key Components and Structure
- **Phases**: The project is phased, with only Phase I detailed here. Future phases (implied but not specified) would build on this, potentially adding web UIs, databases, cloud deployment, event-driven architecture, Kubernetes orchestration, and AI enhancements. Phase I is strictly limited to an in-memory CLI app.
- **Spec-Driven Development with Spec-Kit Plus**: This appears to be a custom or conceptual framework for development:
  - **Constitution**: A foundational prompt or file that defines the AI's behavior, rules, and constraints. It overrides all other instructions and ensures strict adherence to specs.
  - **Specs History**: A folder tracking all specification files over time, treating each as the "single source of truth." No merging or invention of features; conflicts resolved by the latest spec.
  - **Implementation Rules**: Code generation is AI-driven (via Qwen), but must be precise, using only in-memory structures, Python 3.13+, and clean code principles (clarity, simplicity, single responsibility). No databases, files, or scalability features in Phase I.
- **Features for Phase I**:
  - **Add**: Create a new todo with id (int), title (str), description (str), completed (bool, default False).
  - **View**: List all todos with status (e.g., Pending/Completed).
  - **Update**: Modify title or description by ID.
  - **Delete**: Remove a todo by ID.
  - **Mark Complete**: Set completed to True by ID.
- **Data Rules**: Todos are ephemeral (runtime-only), stored in memory (e.g., list of dicts). No persistence.
- **CLI Rules**: Command-line based, concise output, handle invalid inputs gracefully (no crashes).
- **Technology Stack**:
  - Python 3.13+.
  - UV (likely the `uv` tool for Python project management, e.g., for virtual environments and dependencies).
  - Spec-Kit Plus (the spec-driven methodology).
- **Deliverables**:
  - **GitHub Repository**:
    - Constitution file (e.g., a prompt or Markdown defining AI rules).
    - `specs_history/` folder with sequential spec files (e.g., spec1.md, spec2.md).
    - `/src/` folder with generated Python code (logical structure, e.g., main.py with functions).
    - README.md: Setup instructions (e.g., install UV, Python, run the app).
  - **Working App**: Demonstrates all 5 features via console interactions.
- **Platform Considerations**: Windows users must use WSL 2 for a Linux-like environment. Provided commands for setup ensure compatibility (install WSL, set default to version 2, install Ubuntu 22.04).

#### Strengths and Benefits
- **Educational Value**: Teaches iterative development, spec adherence, and AI-assisted coding without manual boilerplate.
- **Scalability Simulation**: Starts simple to build foundational skills, preparing for complex phases (e.g., microservices, AI integration).
- **Clean Code Emphasis**: Promotes principles like single responsibility, avoiding premature optimization.
- **AI Role**: Qwen (or similar AI) is constrained to generate code only from specs, simulating a "spec-to-code" pipeline.

#### Potential Challenges and Constraints
- **Strict Boundaries**: No invention of features—e.g., cannot add user auth, persistence, or AI elements in Phase I. This ensures focus but requires clear specs.
- **Ambiguity Handling**: AI must ask for clarification if specs are unclear.
- **Phase Limitation**: Currently only Phase I; future phases would require new specs/constitutions.
- **Dependencies**: Relies on UV for project setup; no external libs beyond core Python.
- **Testing/Validation**: App must handle edge cases (e.g., invalid IDs, empty inputs) gracefully.
- **Repo Structure**: Must be organized for history tracking; no merging specs.
- **WSL Requirement for Windows**: Ensures Unix-like environment, avoiding Windows-specific issues (e.g., path handling).

#### Recommendations for Implementation
- Start by defining the constitution (as requested) to guide the AI.
- Create initial spec file for Phase I features.
- Use AI to generate code iteratively, committing specs and code to GitHub.
- For evolution, add new phases via updated specs (e.g., Phase II might introduce web API).
- Ensure README includes: `uv venv`, `uv pip install` (if needed, though Phase I likely needs none), `python src/main.py`.

This analysis covers the project holistically based on the provided details. If more phases or external resources (e.g., what "Spec-Kit Plus" exactly entails beyond the description) are needed, I can use tools like web_search for clarification.

### Constitution Prompt
Below is the constitution prompt, written as a complete, self-contained system prompt for the AI (Qwen) to follow. It mirrors the structure and rules from similar examples, tailored to this project. This can be saved as a file (e.g., `constitution.md` or `constitution.txt`) in the GitHub repo.

```
You are Qwen, acting as a SPEC-DRIVEN SOFTWARE ENGINEER.

Your sole responsibility is to generate Python code strictly based on the provided specifications.

This project is "The Evolution of Todo".
You are currently operating in Phase I ONLY.

You MUST NOT:
- Invent features not explicitly defined in the spec
- Add future scalability, cloud, AI, or distributed concepts
- Use databases, files, or persistent storage
- Introduce frameworks or unnecessary abstractions
- Modify behavior from earlier specs unless the new spec says so
- Add any dependencies beyond core Python (no pip installs required in Phase I)

You MUST:
- Treat each specification file as the single source of truth
- Implement exactly the five required features: Add, View, Update, Delete, Mark Complete
- Use in-memory data structures only (e.g., list of dictionaries)
- Follow clean code principles: clarity, simplicity, single responsibility
- Structure Python code logically (e.g., functions for each feature, a main loop for CLI)
- Use Python 3.13+ syntax
- Ask for clarification if a requirement is ambiguous
- Use UV for project management if specified in setup, but generate pure Python code

Data Rules:
- Todos exist only during program runtime
- Each todo contains: id (int, auto-incrementing), title (str), description (str), completed (bool, default False)

CLI Rules:
- Application is command-line based
- Output must be concise and human-readable (e.g., formatted lists, error messages)
- Handle invalid input gracefully without crashing (e.g., try-except for IDs, check empty strings)

Spec-Kit Plus Rules:
- Never bypass specifications
- Never merge multiple specs into one implementation
- Respect spec history (reference specs_history folder)
- Follow the latest spec in case of conflict
- Generate code in /src folder (e.g., main.py)

Documentation Rules:
- Do not explain code unless explicitly asked
- Do not add unnecessary comments
- Do not include boilerplate not required by the spec
- For README.md, include basic setup: Install UV, create venv, run python src/main.py

Setup Rules (for README):
- Recommend WSL 2 for Windows users with provided commands
- Use UV for virtual environment: uv venv, source .venv/bin/activate (or equivalent)

If a request violates this constitution, you must refuse and clearly state the violated rule.

This constitution overrides all other instructions.
```

## Response snapshot

## Constitution Update Summary

I have successfully updated the project constitution at `.specify/memory/constitution.md` with the following details:

- **New Version**: 1.0.0 (Initial version for "The Evolution of Todo" project)
- **Version Bump Rationale**: This is the initial constitution for the project, establishing the foundational principles for the todo application evolution project.

### Key Changes Made:
1. Replaced all placeholder tokens with concrete values based on the project context
2. Defined 6 core principles aligned with the spec-driven development approach:
   - Spec-Driven Development
   - Phase-Based Implementation
   - Clean Code and Simplicity
   - In-Memory Data Management
   - Robust CLI Interface
   - Spec Compliance Verification
3. Added sections for Technology Stack Requirements and Development Workflow
4. Included governance rules specific to this project

### Files Flagged for Manual Follow-up:
- `.specify/templates/plan-template.md` - The "Constitution Check" section should reference the new principles
- `.specify/templates/spec-template.md` - Should ensure alignment with spec-driven approach
- `.specify/templates/tasks-template.md` - Should reflect the independent testing principle
- `.specify/templates/commands/*.md` - Should be reviewed for any outdated references

### Suggested Commit Message:
`docs: create initial constitution for The Evolution of Todo project v1.0.0`

The constitution is now ready and reflects the specific requirements for the todo application evolution project, emphasizing spec-driven development and phased implementation from a CLI-based application to more complex systems in future phases.

## Outcome

- ✅ Impact: Created initial project constitution for "The Evolution of Todo"
- 🧪 Tests: No tests required for this documentation task
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Ready to create feature specifications based on this constitution
- 🧠 Reflection: The constitution properly establishes the foundational rules for spec-driven development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for this task
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating the first feature specification for the todo CLI app