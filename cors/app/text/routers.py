import os
import pickle
from fastapi import APIRouter, Body
from app.text.service import TextService
from app.autocomplete.autocomplete import predire_prochain_mot

router = APIRouter(prefix="/text", tags=["text"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.normpath(os.path.join(BASE_DIR, "..", "teny_malagasy.csv"))
MODEL_FILE = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "malagasy_model.pkl"))

MODEL = None
if os.path.exists(MODEL_FILE):
    with open(MODEL_FILE, 'rb') as f:
        MODEL = pickle.load(f)

@router.get("/analyze")
def analyze_text(text: str):
    closest_word, distance = TextService.find_closest_word(text, CSV_FILE)
    print(f"Mot le plus proche : {closest_word}, Distance : {distance}")
    return { "closest_word": closest_word }

@router.post("/autocomplete")
def autocomplete_text(text: str = Body(..., media_type="text/plain")):
    global MODEL
    if MODEL is None and os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, 'rb') as f:
            MODEL = pickle.load(f)

    suggestions = predire_prochain_mot(MODEL, text) if MODEL else []

    return {
        "words": suggestions,
        "count": len(suggestions)
    }

