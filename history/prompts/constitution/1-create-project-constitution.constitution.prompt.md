---
id: 1
title: create-project-constitution
stage: constitution
date: 2026-02-05
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, spec-driven-development, ai-native-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```text
Project: Evolution of Todo - AI-Native Full-Stack Application (Console → Web → AI Chatbot → Kubernetes → Cloud)

Core Principles:
- Spec-Driven Development: No code without approved specifications
- AI-Assisted Implementation: Claude Code generates all code from specs
- Iterative Refinement: Refine specs until correct output
- Cloud-Native Architecture: Scalable, distributed systems
- Event-Driven Design: Loosely coupled services via events
- Reusable Intelligence: Skills and agents created once, used across all phases

Phase-Specific Standards:

PHASE I - Console App:
- Python 3.13+, in-memory storage (lists/dicts)
- CLI interface with clear prompts
- Task Model: id, title, description, completed, created_at
- Clean code: modular functions, single responsibility
- Graceful error handling and input validation

PHASE II - Full-Stack Web:
- Frontend: Next.js 16 (App Router), TypeScript, Tailwind CSS
- Backend: FastAPI with async/await
- Database: Neon PostgreSQL with SQLModel ORM
- Auth: Better Auth with JWT tokens
- API: RESTful, stateless, proper HTTP codes
- Security: JWT verification, user data isolation
- Structure: Monorepo with /frontend and /backend

PHASE III - AI Chatbot:
- UI: OpenAI ChatKit
- AI: OpenAI Agents SDK
- Tools: Official MCP SDK (add_task, list_tasks, complete_task, delete_task, update_task)
- Stateless chat endpoint, conversation state in database
- Models: tasks, conversations, messages tables
- Natural language understanding with friendly responses

PHASE IV - Local Kubernetes:
- Docker containerization with multi-stage builds
- Kubernetes (Minikube) with Helm Charts
- AI DevOps: kubectl-ai and kagent
- ConfigMaps for config, Secrets for credentials
- Services: Frontend (NodePort), Backend (ClusterIP), External DB

PHASE V - Cloud Deployment:
- Cloud: DigitalOcean DOKS or Oracle OKE
- Kafka: Redpanda Cloud or Strimzi self-hosted
- Dapr: Pub/Sub, State, Service Invocation, Jobs API, Secrets
- Topics: task-events, reminders, task-updates
- Advanced Features: recurring tasks, due dates, priorities, tags, search, filter, sort
- CI/CD: GitHub Actions

Architecture Rules:
- Microservices: independently deployable
- Stateless services: all state in DB or queue
- API-First: well-documented REST APIs
- Auth: JWT shared between frontend/backend
- Database: Neon PostgreSQL (single source of truth)
- Secrets: environment variables or K8s Secrets (no hardcoding)

Code Quality:
- Python: type hints, async/await, Pydantic models, HTTPException
- TypeScript: strict mode, proper types, minimal 'any'
- React: Server Components default, Client only when needed
- Database: SQLModel, proper indexes, foreign keys
- Documentation: README.md, CLAUDE.md, /specs folder

Spec-Driven Workflow:
1. /sp.constitution - Define principles
2. /sp.specify - Define WHAT (requirements, user stories, acceptance criteria)
3. /sp.plan - Define HOW (architecture, components, data flow)
4. /sp.tasks - Define atomic work units
5. /sp.implement - Generate code

Success Criteria:
- Phase I: Console app with Basic Level features (Add, Delete, Update, View, Mark Complete)
- Phase II: Web app on Vercel with multi-user auth
- Phase III: Chatbot managing todos via natural language
- Phase IV: App on Minikube, accessible via port-forward
- Phase V: Cloud K8s with Kafka, Dapr, advanced features

Deliverables:
- Public GitHub repo: /specs, /frontend, /backend, /k8s
- Deployed URLs: Vercel (Phase II+), Cloud K8s (Phase V)
- Demo video: under 90 seconds
- Documentation: README.md, CLAUDE.md, all specs

Bonus Strategy:
- Reusable Intelligence: skills/subagents in Phase II (+200 pts)
- Cloud-Native Blueprints: K8s/Helm templates (+200 pts)
- Urdu support (+100 pts)
- Voice commands (+200 pts)

Non-Negotiables:
- Strict Spec-Driven Development workflow
- Each phase builds on previous (no restarts)
- Database schema supports all phases
- MCP tools stateless and DB-backed
- Helm charts for K8s deployments
- Dapr abstraction for Kafka
- Externalized secrets
```

## Response snapshot

Created comprehensive project constitution for the Evolution of Todo - AI-Native Full-Stack Application. The constitution encompasses all specified principles, phase-specific standards, architecture rules, code quality standards, spec-driven workflow, success criteria, deliverables requirements, bonus strategy implementation, and non-negotiable requirements. The document is organized into clear sections with declarative statements that establish mandatory practices and guidelines for the entire project lifecycle.

## Outcome

- ✅ Impact: Created complete project constitution document that establishes governance and principles for all 5 phases of development
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with comprehensive principles and standards
- 🔁 Next prompts: Continue with /sp.specify to define specific feature requirements
- 🧠 Reflection: The constitution successfully captures all requirements from the user input and organizes them into actionable principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All requirements from user input captured in constitution
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin specification phase with /sp.specify