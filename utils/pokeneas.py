import random
import pandas as pd



def createPokeNeas():
    pokeneas = []

    phrases = [
        "Get ready to be inspired…", 
        "See rejection as redirection.",
        "There is beauty in simplicity.",
        "You can’t be late until you show up.",
        "Maybe life is testing you. Don’t give up.",
        "Impossible is just an opinion.",
        "Alone or not you gonna walk forward.",
    ]

    df = pd.read_csv("utils/pokemon.csv")
    print(df.head())
    for index, row in df.head(10).iterrows():
        pokenea = {
            'id': row['pokedex_number'],
            'name': row['name'],
            'height': row['height_m'],
            'abilities': row['abilities'],
            'image_url': f'https://storage.googleapis.com/pokeneass/00{index+1}.png',
            'phrase': random.choice(phrases)
        }
        pokeneas.append(pokenea)

    return pokeneas


