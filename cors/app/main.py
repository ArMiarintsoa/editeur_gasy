import os
import sys
from typing import Union

# S'assurer que le dossier racine 'cors' est dans sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.text.routers import router as text_router

app = FastAPI(title="Text editor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],        # tous les headers
)

app.include_router(text_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)