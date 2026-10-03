from bs4 import BeautifulSoup
import regex as re

def parse_words(html):
    soup = BeautifulSoup(html, "lxml")    
    all_words = []

    items = soup.find_all("p", class_="and clearfix")

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
