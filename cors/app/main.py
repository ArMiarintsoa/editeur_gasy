from typing import Union
from app.text.routers import router as text_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Text editor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],        # tous les headers
)

app.include_router(text_router)