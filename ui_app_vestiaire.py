import streamlit as st
from PIL import Image

# Configuration de la page principale
st.set_page_config(page_title="App Mode", layout="wide")

# Titre de l'application
st.title("Assistant Mode - Choisissez vos Tenues")

# Barre latérale avec les onglets
menu = st.sidebar.selectbox("Menu", ["Accueil", "Vestiaire", "Générer des Tenues"])

# Dictionnaire pour stocker les vêtements téléchargés
if 'vestiaire' not in st.session_state:
    st.session_state.vestiaire = {}

# Fonction pour afficher une barre de défilement horizontale
def display_horizontal_images(images):
    # On crée une div avec une barre de défilement horizontale
    st.markdown("""
        <style>
        .scrolling-wrapper {
            display: flex;
            flex-direction: row;
            overflow-x: auto;
            white-space: nowrap;
        }
        .scrolling-wrapper img {
            margin-right: 10px;
            border-radius: 10px;
        }
        </style>
        <div class="scrolling-wrapper">
    """, unsafe_allow_html=True)

    # Ajout des images sous forme d'éléments HTML
    for image in images:
        # Convertir l'image en base64 pour l'afficher
        buffered = image_to_base64(image)
        img_html = f'<img src="data:image/png;base64,{buffered}" width="150" height="200">'
        st.markdown(img_html, unsafe_allow_html=True)

    # Fermer la div
    st.markdown("</div>", unsafe_allow_html=True)

# Fonction pour convertir une image en base64 pour l'affichage HTML
def image_to_base64(image):
    from io import BytesIO
    import base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Onglet Accueil
if menu == "Accueil":
    st.header("Bienvenue dans votre assistant mode !")
    st.write("Ajoutez vos vêtements dans l'onglet **Vestiaire** et générez des tenues dans l'onglet **Générer des Tenues**.")

# Onglet Vestiaire
elif menu == "Vestiaire":
    st.header("Votre Vestiaire")
    
    # Ajout de vêtements via des images
    uploaded_files = st.file_uploader("Ajoutez des photos de vos vêtements", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
    
    if uploaded_files:
        for file in uploaded_files:
            image = Image.open(file)
            st.session_state.vestiaire[file.name] = image
            st.image(image, caption=file.name, use_column_width=False, width=400)
    
    if st.button("Sauvegarder le vestiaire"):
        st.success("Vêtements sauvegardés avec succès !")

# Onglet Générer des Tenues
elif menu == "Générer des Tenues":
    st.header("Générer des Tenues")
    
    if st.session_state.vestiaire:
        # Afficher les images dans une barre horizontale
        images = list(st.session_state.vestiaire.values())
        display_horizontal_images(images)
    
        if st.button("Générer une tenue"):
            # Ici tu pourras ajouter l'algorithme pour générer des tenues
            st.write("Tenue générée (en attente de l'algorithme) !")
    else:
        st.warning("Veuillez ajouter des vêtements dans l'onglet **Vestiaire**.")
