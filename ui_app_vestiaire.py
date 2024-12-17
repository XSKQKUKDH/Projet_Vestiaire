import streamlit as st
from PIL import Image
from backend import *
import os

# Configuration de la page principale
st.set_page_config(page_title="Vestiaire", layout="wide")

# Barre latérale avec les onglets
menu = st.sidebar.selectbox("Menu", ["Accueil", "Vestiaire", "Génération de tenue"])

# Dictionnaire pour stocker les vêtements téléchargés
if 'vestiaire' not in st.session_state:
    st.session_state.vestiaire = []

if 'importation_vetement' not in st.session_state:
    st.session_state.importation_vetement = False

if 'vetement_selectione' not in st.session_state:
    st.session_state.vetement_selectionne = None

categories_vetements = [
    "T-shirt",
    "Pull",
    "Sweatshirt",
    "Débardeur",
    "Chemise",
    "Blouse",
    "Pantalon",
    "Jean",
    "Jogging",
    "Short",
    "Jupe",
    "Veste",
    "Blouson",
    "Manteau",
    "Doudoune",
    "Gilet",
    "Robe",
    "Baskets",
    "Bottes",
    "Sandales",
    "Écharpe",
    "Chapeau",
    "Bonnet",
    "Gants",
]

# Onglet Accueil
if menu == "Accueil":
    st.header("Bienvenue sur Vestiaire !")
    st.write("Ajoutez vos vêtements dans l'onglet **Vestiaire** et générez des tenues dans l'onglet **Générer des Tenues**.")
    with st.expander('A propos'):
        st.write('Cette application vous permet de faire un vestiaire de tous vos vêtements et pourra vous générer des tenues !')

# Onglet Vestiaire
elif menu == "Vestiaire":
    st.header("Votre Vestiaire")

        
    if st.button('importer_vetements'):
        st.session_state.importation_vetement = True

    if st.session_state.importation_vetement is True:
        nom = st.text_input('Nom du vêtement', placeholder='ex : T-shirt NYC')
        categorie = st.selectbox('Catégorie', options=categories_vetements)
        couleur = st.selectbox('Couleur', options=["Rouge", "Bleu", "Vert", "Jaune", "Noir", "Blanc", "Gris", "Rose", "Orange", "Marron", "Violet", "Beige", "Turquoise", "Bordeaux", "Kaki", "Bleu marine"])
        style = st.text_input('Style du vetement', placeholder='ex : baggy')
        marque = st.text_input('Marque', placeholder='Carhartt')
        images_importe = st.file_uploader("Ajoutez des photos de vos vêtements", accept_multiple_files=True, type=["png", "jpg", "jpeg", 'webp']) # Ajout de vêtements via des images

        if st.button('Enregistrer vêtement'):
            ajoute_vetement(nom, categorie, couleur, style, images_importe, marque)
            st.session_state.importation_vetement = False
            st.rerun()

    if st.session_state.importation_vetement is False:

        if st.session_state.vetement_selectionne is None:
            # Titre de la section
            st.title("Galerie de vêtements")

            with open('vestiaire.json', 'r') as file:
                vetements = json.load(file)

            # Afficher les vêtements sous forme de galerie
            cols = st.columns(4)  # Nombre de colonnes dans la galerie
            for i, vetement in enumerate(vetements):
                with cols[i % 4]:  # Alterner entre les colonnes
                    st.image(vetement["lien_image"], caption=vetement["nom"], use_column_width=True)
        
        else:
            st.write("Here's the information about...")

elif menu == "Génération de tenue":
    st.title("Ici, générez vos tenues !")

    if st.button('Générer tenue automatiquement'):
        tenue = genere_tenue()
        

    elif st.button('Générer tenue manuellement'):
        pass

