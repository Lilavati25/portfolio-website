# Portfolio Backend - FastAPI

Backend API for Lilavati Mhaske's Portfolio Website

## Tech Stack
- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Server**: Uvicorn

## Setup

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Development Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: http://localhost:8000

## API Endpoints

- `GET /` - API root information
- `GET /api/about` - Get about information
- `GET /api/projects` - Get all projects
- `GET /api/projects/{id}` - Get specific project
- `GET /api/experience` - Get work experience
- `GET /api/skills` - Get skills and competencies

## API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── portfolio.py     # Portfolio API endpoints
│   ├── models/              # Database models (future)
│   └── schemas/             # Pydantic schemas (future)
├── requirements.txt
└── README.md
```

## Development

### Adding New Endpoints
Add new routes in `app/api/portfolio.py`

### CORS Configuration
Frontend URL is configured in `app/main.py` for local development
