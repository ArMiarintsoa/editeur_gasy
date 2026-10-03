import pandas as pd
import os

def save_data(data, filename="teny_malagasy.csv", key_column="word"):
    """
    data : liste de mots (strings)
    """

    # créer le DataFrame correctement
    new_df = pd.DataFrame(data, columns=[key_column])

    if os.path.exists(filename):
        old_df = pd.read_csv(filename, encoding="utf-8")

        combined_df = pd.concat([old_df, new_df], ignore_index=True)

        combined_df = combined_df.drop_duplicates(subset=[key_column])

    else:
        combined_df = new_df

    combined_df.to_csv(filename, index=False, encoding="utf-8")

    print(f"Fichier mis à jour : {len(combined_df)} mots")
