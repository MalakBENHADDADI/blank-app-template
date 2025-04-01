import streamlit as st

# Fonction pour afficher une carte
def display_card(title, description, image_url, link_url):
    # Conteneur pour la carte
    with st.container():
        st.markdown(f"<div style='border: 1px solid #ddd; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>", unsafe_allow_html=True)
        
        # Image
        st.image(image_url, width=150)
        
        # Titre
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
        
        # Description
        st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
        
        # Lien vers une autre page ou une action
        if st.button('En savoir plus', key=title):
            st.markdown(f"[Cliquez ici pour en savoir plus]({link_url})")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Liste de données représentant les cartes
cards_data = [
    {
        'title': 'Carte 1',
        'description': 'C’est une carte avec un lien vers plus d\'informations.',
        'image_url': 'https://via.placeholder.com/150',
        'link_url': 'https://www.example.com'
    },
    {
        'title': 'Carte 2',
        'description': 'Voici une autre carte avec une description différente.',
        'image_url': 'https://via.placeholder.com/150',
        'link_url': 'https://www.example.com'
    },
    {
        'title': 'Carte 3',
        'description': 'Encore une autre carte, pour afficher plusieurs cartes.',
        'image_url': 'https://via.placeholder.com/150',
        'link_url': 'https://www.example.com'
    }
]

# Titre de la page
st.title("Page avec des cartes")

# Boucle pour afficher les cartes
for card in cards_data:
    display_card(
        title=card['title'],
        description=card['description'],
        image_url=card['image_url'],
        link_url=card['link_url']
    )

