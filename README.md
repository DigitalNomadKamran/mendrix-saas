# Mendrix Rentals SaaS

This project delivers a lightweight Software-as-a-Service experience for vacation rental managers.
Owners can upload property listings, connect their Airbnb/Booking.com channels, and receive
AI-guided optimization suggestions and partnership leads in one dashboard.

The repository contains a FastAPI backend with a SQLite datastore and a Vite + React frontend.

## Features

- **Property onboarding** – capture listing basics, nightly rate, and occupancy.
- **Channel connectivity** – log Airbnb/Booking.com credentials per listing.
- **AI-style insights** – deterministic heuristics surface pricing tweaks and content upgrades.
- **Lead generation** – curated outreach ideas for corporate housing and influencer partners.

## Project structure

```
backend/   # FastAPI application (SQLite + SQLAlchemy)
frontend/  # Vite + React single-page app (React Query + Axios)
```

## Getting started

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs on `http://localhost:8000`. A SQLite database file (`mendrix.db`) will be created
automatically.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The Vite dev server starts on `http://localhost:5173`. If your backend is on another origin,
set `VITE_API_URL` in a `.env` file (e.g. `VITE_API_URL=http://localhost:8000`).

## Example workflow

1. Add a property from the left-hand panel.
2. Select the property to view its accounts and insights.
3. Connect Airbnb/Booking.com accounts for the active property.
4. Open the insights card to generate optimization suggestions and partnership leads.

## API quick reference

| Endpoint | Description |
| --- | --- |
| `POST /properties/` | Create a new property listing |
| `GET /properties/` | List all properties |
| `POST /accounts/` | Attach an Airbnb/Booking account to a property |
| `GET /accounts/?property_id=` | Fetch accounts (optionally filtered by property) |
| `GET /insights/{id}/suggestions` | Generate or return cached optimization suggestions |
| `GET /insights/{id}/leads` | Generate or return cached lead recommendations |

## Testing the API

Interact directly with the backend using FastAPI's Swagger UI at `http://localhost:8000/docs`.

## Deployment notes

- Swap SQLite for PostgreSQL/MySQL by updating `SQLALCHEMY_DATABASE_URL` in `backend/app/database.py`.
- Harden account storage or integrate OAuth flows before connecting to live OTA APIs.
- Replace the heuristic `services.generate_suggestions` with an AI provider (OpenAI, etc.).
