from scraper.fetcher import fetch_html
from scraper.saver import save_data
from sites.baiboly.baiboly_text import build_malagasy_text_dataset
from bs4 import BeautifulSoup
import os
import regex as re

def run_scraping():
    url = "https://www.tiatanindrazana.mg/fandriampahalemana/nampitandrina-ny-fds-misy-nampiditra-fitaovam-piadiana-65689.php"

    html = fetch_html(url)
    words = parse(html)
    save_data(words, "teny_malagasy.csv", "word")
    build_malagasy_text_dataset(html)
    print("=== PROCESSUS TERMINÉ ===")

def build_malagasy_text_dataset(
    html,
    output_file="malagasy_corpus.txt",
    min_word_length=1
):
    """
    Crée un fichier texte prêt pour l'entraînement ML à partir d'une page HTML
    """

    soup = BeautifulSoup(html, "lxml")

    paragraphs = soup.find_all("p")

    lines = []

    for p in paragraphs:
        print(p)
        
        text = p.get_text(" ", strip=True)

        # garder uniquement les lettres (Unicode)
        text = re.sub(r"[^\p{L}]", " ", text)

        # normaliser
        text = re.sub(r"\s+", " ", text).strip().lower()

        # filtrer mots courts
        words = [w for w in text.split(" ") if len(w) >= min_word_length]

        if len(words) >= 3:  # garder phrases utiles
            lines.append(" ".join(words))

    # écrire dans le fichier (mode append)
    os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)

    with open(output_file, "a", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"Dataset mis à jour : {len(lines)} lignes ajoutées")

    return lines
    

def parse(html):
    soup = BeautifulSoup(html, "lxml")    
    all_words = []

    items = soup.find_all("div", class_="contenu")

    for item in items:        
        text = item.get_text(strip=True)                

        # 1️⃣ Remplacer tout ce qui n'est PAS une lettre par un espace
        words = re.sub(r"[^a-zA-Z]", " ", text)

        # 2️⃣ Supprimer les espaces multiples
        words = re.sub(r"\s+", " ", words).strip()

        # 3️⃣ Tout mettre en minuscules
        words = words.lower()

        # 4️⃣ Transformer en liste de mots
        words = words.split(" ")

        # concaténation + suppression des doublons
        all_words = list(dict.fromkeys(all_words + words))

        print(words)
        print(f"Nombre de mots extraits jusqu'ici : {len(words)}")        

    print("=== EXTRACTION TERMINÉE ===")
    print(all_words)
    print(f"Nombre total de mots uniques : {len(all_words)}")

    return all_words

