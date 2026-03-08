"""FastAPI server wrapping the ADK restaurant concierge agent.

Production-ready with:
- CORS for frontend integration
- Configurable port/host via env vars
- dotenv support
"""

import os
from dotenv import load_dotenv

load_dotenv()

import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from google.adk.cli.fast_api import get_fast_api_app

ALLOWED_ORIGINS = os.environ.get(
    "CORS_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173"
).split(",")

app = get_fast_api_app(web=True, agents_dir=".")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    reload = os.environ.get("ENV", "development") == "development"
    uvicorn.run("server:app", host=host, port=port, reload=reload)
