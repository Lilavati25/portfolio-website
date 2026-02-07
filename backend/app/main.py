from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import portfolio

app = FastAPI(
    title="Portfolio API",
    description="Backend API for Lilavati Mhaske's Portfolio",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(portfolio.router, prefix="/api", tags=["portfolio"])

@app.get("/")
async def root():
    return {
        "message": "Portfolio API",
        "version": "1.0.0",
        "endpoints": ["/api/about", "/api/projects", "/api/experience", "/api/skills"]
    }
