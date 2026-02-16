# Deployment Guide

## Environment Variables
### Backend
- `PROVIDER_MODE=mock|live`
- `DATABASE_URL=postgresql://stock:stock@postgres:5432/stock_ai`
- `REDIS_URL=redis://redis:6379/0`
- `JWT_SECRET=change_me`

### Frontend
- `NEXT_PUBLIC_API_BASE=http://localhost:8000/api/v1`

## Local Run
1. `docker compose up --build`
2. Frontend: `http://localhost:3000`
3. Backend health: `http://localhost:8000/api/v1/health`

## One-Click (container platform)
- Push repository.
- Configure managed PostgreSQL and Redis.
- Set env vars above.
- Deploy backend and frontend services.

## Notes
- Enable HTTPS and secure cookies for OAuth in production.
- Replace mock adapters with licensed providers before live trading research use.
