# 3D Print AI Business Engine

A modular monorepo for a small 3D-printing business. This first working version includes the foundation for:

- FastAPI backend with health checks and intelligence endpoints
- Next.js + TypeScript + Tailwind frontend
- PostgreSQL + Redis via Docker Compose
- SQLAlchemy models for products, opportunities, printers, and materials
- scoring and cost calculator services
- basic dashboard and acceptance-test flow for the core product intelligence system

## Repository structure

- `backend/` - FastAPI application and Python services
- `frontend/` - Next.js dashboard application
- `infra/` - infrastructure and deployment assets
- `docs/` - product and engineering documentation
- `scripts/` - operational scripts
- `.env.example` - environment configuration placeholders
- `docker-compose.yml` - local dev stack

## Quick start

1. Copy `.env.example` to `.env` and update values.
2. Start services:
   ```bash
   docker compose up --build
   ```
3. Start backend:
   ```bash
   cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
4. Start frontend:
   ```bash
   cd frontend && npm install && npm run dev
   ```
5. Open http://localhost:3000

## Core acceptance flow

This scaffold supports the first working interaction:

- Add a printer
- Add filament
- Add a product opportunity
- Enter material weight, print time and selling price
- Calculate production cost and profit
- Score the opportunity
- Save the product
- View it on the dashboard

## Notes

This is the Phase 1 and Phase 2 foundation for the product intelligence system. Social publishing and advanced AI workflows are intentionally deferred until the core product intelligence system is proven.
