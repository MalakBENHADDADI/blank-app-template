import streamlit as st

# Création du formulaire
with st.form(key='testCareer'):
    # Ajout de champs au formulaire
    name = st.text_input('Nom')
    email = st.text_input('Email')
    age = st.number_input('Âge', min_value=0)
     # Sélection multiple pour les hobbies
    hobbies = st.multiselect(
        'Choisissez vos hobbies',
        options=['Lecture', 'Voyage', 'Musique', 'Sport', 'Cinéma'],
        default=['Musique']  # Option par défaut
    )
    # Ajouter un bouton de soumission
    submit_button = st.form_submit_button(label='Soumettre')

# Afficher les données une fois le formulaire soumis
if submit_button:
    st.write('Nom:', name)
    st.write('Email:', email)
    st.write('Âge:', age)

