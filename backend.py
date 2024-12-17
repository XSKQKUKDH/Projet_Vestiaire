import json
import os
import json
import random

hauts = [
    "T-shirt",
    "Pull",
    "Sweatshirt",
    "Débardeur",
    "Chemise",
    "Blouse",
    "Veste",
    "Blouson",
    "Manteau",
    "Doudoune",
    "Gilet",
    "robe",
    "Gants"
]

bas = [
    "Pantalon",
    "Jean",
    "Jogging",
    "Short",
    "Jupe"
]

chaussures = [
    "Baskets",
    "Bottes",
    "Sandales"
]

couvre_chef = [
    "Écharpe",
    "Chapeau",
    "Bonnet"
]

def ajoute_vetement(nom_vet, categorie, couleur, style, images_importes, marque):

    with open('vestiaire.json', 'r') as file: # Récupère les données du fichier vestiaire.json
        vestiaire = json.load(file)

    for image_importe in images_importes: # Enregistrer l'image dans le dossier local
        chemin_image = os.path.join('images', f'{nom_vet}{len(vestiaire)}')

        with open(chemin_image, "wb") as f:
            f.write(image_importe.getbuffer())
    
    if categorie in hauts:
        type = 'hauts'
    elif categorie in bas:
        type = 'bas'
    elif categorie in chaussures:
        type = 'chaussure'
    elif categorie in couvre_chef:
        type = 'couvre_chef'

    vetement = {
        "nom" : nom_vet,
        "categorie" : type,
        "couleur" : couleur,
        "style" : style,
        "lien_image" : chemin_image,
        "marque" : marque,
        'id' : len(vestiaire),
    }
    vestiaire[type].append(vetement)

    with open('vestiaire.json', 'w') as file: # Met à jour les donnees
        json.dump(vestiaire, file, indent=4)

def genere_tenue(): # Générer une tenue

    with open('vestiaire.json', 'r') as file: # Récupère les données du fichier vestiaire.json
        vestiaire = json.load(file)

    haut_choisi = random.choice(hauts)
    bas_choisi = random.choice(bas)

    tenue = [haut_choisi, bas_choisi]
    return tenue