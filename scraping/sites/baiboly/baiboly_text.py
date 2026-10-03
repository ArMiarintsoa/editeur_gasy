from bs4 import BeautifulSoup
import regex as re
import os

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
