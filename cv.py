import streamlit as st

with st.sidebar:
    st.title("Fallou Sow")

    st.write("Technicien expert en Géomatique au Centre d'Entrepreunariat et développement Technique (CEDT-15) ainsi qu'en Géographie á l'Université Cheikh Anta Diop de Dakar, je mets mes compétences au services de projets technique et de gestions des espaces. Rigoureux, méthodique et á l'aise en travail d'équipe.")

    st.subheader("mail")
    st.write("&#9993;sfallou257357@gmail.com")

    st.subheader("Adresse")
    st.write("&#127968;DAKAR,SÉNÉGAL")

st.subheader("\U0001F4DAFORMATION ACADÉMIQUE")

st.markdown("""
* 2025-2026: Licence en Géographie, Université Cheikh Anta Diop de Dakar
* 2026-2027: Brevet de Technicien Supérieur en Géomatique, CEDT-G15
* 2020-2021: Baccalauréat en Lettres et Sciences Humaines, UCAD
""")

st.subheader("\U0001F528COMPÉTENCES")

col1, col2 = st.columns(2)

with col1:
    st.subheader("GÉOMATIQUE")
    st.markdown("""
     * Maîtrise des Outils SIG (Systemes d'Informations Géographique)

     * Acquisation et traitements des données sur ArcMap

     * Lever Topographique avec Station Total

     * Modélisation Bâtiment 2D sur AutoCAD

     * Anglais Technique

     * Français Technique

     * Modélisation Bâtiment 3D sur SKetchUp

     * Géoréférencement des données spatiales
       """)
with col2:
    st.subheader("GEOGRAPHIE")
    st.markdown("""
     * Gestion Des Ressources Naturelles
     * Étude du climat et des changements climatiques
     * Analyse des risques (inondations, sécheresses")
     """)

st.subheader("\U0001F9F0  OUTILS")
st.markdown("""

* suite Bureautique

* OTC (Outil de Travail Collaboratif)

* ARCgis (Analyse, stockage et exploitation de données SIG")

* Outils de télédétection: Traitement et interprétation d'Image satellites

* Base de données spatiales

* Logiciels modélisation (MNT)

* Théodolites

* Topographie

* Photogrammétrie
""")

st.subheader("\U00002705RÉALISATIONS")

st.markdown("""

* Création de cartes thématique 

* Levés topographiques 

* Numerisation( Bâti, Parcellaire)

* Dessin plan en 2D et 3D
""")







    