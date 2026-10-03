from fastapi import APIRouter, Body
from .service import TextService
from app.autocomplete.autocomplete import predire_prochain_mot, mon_modele
import pickle

router = APIRouter(prefix="/text", tags=["text"])

@router.get("/analyze")
def analyze_text(text: str):
    csv_file = "../teny_malagasy.csv"
    closest_word, distance = TextService.find_closest_word(text, csv_file)
    print(f"Mot le plus proche : {closest_word}, Distance : {distance}")
    return { "closest_word": closest_word }


@router.post("/autocomplete")
def autocomplete_text(text: str = Body(..., media_type="text/plain")):    
    import os
    def charger_modele(filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.normpath(os.path.join(base_dir, filename))
        with open(abs_path, 'rb') as f:
            return pickle.load(f)

    # Chargement initial
    MODEL = charger_modele('../../malagasy_model.pkl')
    suggestions = predire_prochain_mot(MODEL, text)

    return {
        "words": suggestions,
        "count": len(suggestions)
    }
