import requests
from time import sleep

def fetch_html(url):    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    sleep(0.3)  # pause pour ne pas surcharger le serveur
    return response.text

