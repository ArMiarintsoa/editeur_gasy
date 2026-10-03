import re
from collections import defaultdict, Counter
import pickle

def charger_et_nettoyer_corpus(filepath):
    import os
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_dir, '../malagasy_corpus.txt')
    abs_path = os.path.normpath(abs_path)
    with open(abs_path, 'r', encoding='utf-8') as f:
        texte = f.read().lower()
    
    tokens = re.findall(r'\b\w+\b', texte)
    return tokens

def construire_modele_trigramme(tokens):
    
    model = defaultdict(Counter)
    
    for i in range(len(tokens) - 2):
        w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
        model[(w1, w2)][w3] += 1
        
    return model

def predire_prochain_mot(model, texte_entree, nb_suggestions=3):
   
    mots = re.findall(r'\b\w+\b', texte_entree.lower())
    
    if len(mots) < 2:
        return "Veuillez entrer au moins deux mots."
    
    
    contexte = (mots[-2], mots[-1])
    
    if contexte in model:
        
        suggestions = model[contexte].most_common(nb_suggestions)
        return [word for word, count in suggestions]
    else:
        return [] 



def sauvegarder_modele(model, filename):
    
    with open(filename, 'wb') as f:
        pickle.dump(dict(model), f)
    print(f"Modèle enregistré avec succès dans {filename}")


tokens = charger_et_nettoyer_corpus('../malagasy_corpus.txt')
mon_modele = construire_modele_trigramme(tokens)
sauvegarder_modele(mon_modele, 'malagasy_model.pkl')

