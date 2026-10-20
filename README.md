# EduMore

EduMore is an academic productivity platform designed to help faculty and academic management create, review, organize, and monitor learning content and academic work.

The initial focus is on faculty and management workflows. Student-facing functionality can be introduced in a later phase.

## Core Modules

### 1. Curriculum Designer
- Research relevant and credible sources.
- Generate structured curricula from beginner to advanced levels.
- Organize topics, learning outcomes, and estimated durations.
- Present a curriculum roadmap for faculty review.
- Keep source references available for verification.

### 2. Notes and Assessment Generator
- Research and synthesize original learning notes.
- Generate practice questions, assessments, and solutions.
- Run quality checks on generated content.
- Require faculty review before official publication.
- Export approved content to PDF.

### 3. Faculty and Academic Management
- Track course and syllabus progress.
- Support workload and course planning.
- Identify pending work and potential delays.
- Provide management-level progress reports.

## Technology Stack

- **Backend:** Python, FastAPI
- **Frontend:** React, Tailwind CSS
- **Database:** PostgreSQL
- **ORM and migrations:** SQLAlchemy, Alembic
- **AI workflow orchestration:** LangGraph
- **Data validation:** Pydantic
- **Testing:** pytest

Dependency versions are intentionally expressed as compatible ranges rather than permanently fixed versions. Before deployment, resolve and test a compatible dependency set and maintain a lock file or pinned deployment requirements.

## High-Level Architecture

```text
frontend/  ->  FastAPI API  ->  Services  ->  Repositories  ->  PostgreSQL
                                  |
                                  v
                            AI Workflows
                         (LangGraph + LLM)
                                  |
                                  v
                         Research and Quality
```

The frontend communicates with the backend through versioned API endpoints. Business logic belongs in services, database access belongs in repositories, and AI workflows are kept separate from API handlers.

## Planned Repository Structure

```text
EduMore/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   ├── core/
│   │   ├── db/
│   │   │   └── models/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── ai/
│   │   │   ├── llm/
│   │   │   ├── workflows/
│   │   │   ├── research/
│   │   │   ├── prompts/
│   │   │   └── quality/
│   │   ├── integrations/
│   │   ├── workers/
│   │   └── utils/
│   ├── migrations/
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── api/
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── public/
│   └── src/
│       ├── app/
│       ├── assets/
│       ├── components/
│       ├── layouts/
│       ├── pages/
│       ├── features/
│       ├── services/
│       ├── hooks/
│       ├── utils/
│       └── styles/
├── docs/
│   ├── requirements/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   └── testing/
└── README.md
```

This is the planned structure. Directories and modules should be created as implementation begins; empty directories do not need to be committed.

## Prerequisites

Install the following before running the project:

- Python 3.11 or another Python version verified against the chosen dependency set.
- Node.js LTS and npm.
- PostgreSQL.
- Git.

## Backend Setup

Run commands from the repository root.

### 1. Create and activate a virtual environment

**Windows PowerShell**
```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
cd backend
python3.11 -m venv .venv
source .venv/bin/activate
```

### 2. Install backend dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure environment variables

Create `backend/.env` using `.env.example` as a template. Set the PostgreSQL connection string and any required LLM or research-provider credentials.

Never commit `.env` files, passwords, API keys, or other secrets to Git.

### 4. Run the API

Once `backend/app/main.py` contains the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The local API documentation is normally available at:

- `/docs`
- `/redoc`

These routes are served by the running FastAPI application.

## Frontend Setup

Once the React application has been initialized in `frontend/`:

```bash
cd frontend
npm install
npm run dev
```

Frontend dependencies are managed separately through `package.json` and the package-manager lock file.

## Development Principles

- Keep API endpoints thin; put business logic in services.
- Keep database access in repositories.
- Validate API inputs and outputs with Pydantic schemas.
- Keep LLM-provider integrations separate from LangGraph workflows.
- Store source references for generated educational content.
- Validate generated content and require faculty approval before official publication.
- Track long-running jobs with explicit status and useful error messages.
- Add unit, integration, and API tests as each feature is implemented.
- Use database migrations for schema changes.
- Keep secrets on the backend, never in React client-side code.
- Apply institution-level authorization and data isolation before storing real institutional data.
- Avoid claiming generated content is factually correct without verification.

## Current Development Status

The project is in the planning and initial setup stage. The high-level modules and core technology choices have been identified. The detailed database schema, API contracts, authentication and authorization rules, LLM provider, background-job implementation, and test acceptance criteria must be finalized as development proceeds.

## License

No license has been selected yet. Add a license before publishing or distributing the project.
