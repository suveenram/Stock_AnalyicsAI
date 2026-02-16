# Stock Analytics AI

A dual-market (India + US) research web app for retail investors featuring fundamentals, technicals, AI explainability, and allocation guidance.

## Included Deliverables
- PRD, architecture, DB schema, API spec, sitemap/wireframes (`docs/`).
- Backend FastAPI code with pluggable provider interfaces and mock adapters (`backend/app`).
- Frontend Next.js dashboard with stock details, compare page, beginner/pro toggle, disclaimer, and export actions (`frontend/app`).
- Seeded mock dataset (`backend/app/data/mock_data.py`, `seed.py`).
- Unit tests for critical calculations (`backend/app/tests/test_calculations.py`).
- Docker deployment and env guidance (`docker-compose.yml`, `docs/DEPLOYMENT.md`).

## Quickstart (Local)

### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
NEXT_PUBLIC_API_BASE=http://localhost:8000/api/v1 npm run dev
```

### Test
```bash
cd backend
PYTHONPATH=. pytest app/tests -q
```

## Compliance
This app is educational only and not investment advice. It avoids guaranteed-return language and uses probability ranges + assumptions for recommendation confidence.


## Offline Preview (no dependency install)
```bash
cd preview
python3 -m http.server 4173
```
Then open `http://localhost:4173` for a static prototype preview when package registries are unavailable.
