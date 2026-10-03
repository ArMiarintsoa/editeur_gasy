boky = {'Jenezy': 50, 'Eksaody': 40, 'Levitika': 27, 'Fanisana': 36, 'Detoronomy': 34, 'Josoe': 24, 'Mpitsara': 21}

from scraper.fetcher import fetch_html
from scraper.parser import parse_words
from scraper.saver import save_data
from sites.baiboly.baiboly_text import build_malagasy_text_dataset

def run_scraping():
    for book, chapters in boky.items():
        for i in range(1, chapters + 1):
            print(f"Traitement de {book} chapitre {i}...")
            url = f"https://baiboly.katolika.org/boky/{book}/{i}"

            html = fetch_html(url)
            words = parse_words(html)
            save_data(words, "teny_malagasy.csv", "word")
            build_malagasy_text_dataset(html)
            print("=== PROCESSUS TERMINÉ ===")


