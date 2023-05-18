import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

###############################################################################################################################################
##### Preparation

# Configurer la mise en page de la page Streamlit
st.set_page_config(layout="wide")

# Intégrer la police à Streamlit en utilisant @import
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Kalam:wght@700&family=Mogra&family=Roboto&display=swap');</style>", unsafe_allow_html=True)

# image 
image = Image.open('logowild.png')
photo = Image.open('photo profil.jpg')

###############################################################################################################################################
##### Debut de la page

##### TITRE 
st.markdown('<p style=" font-family: Kalam; font-size: 40px;">CV - ANALYSE DE MON PARCOURS PROFESSIONNEL</p>', unsafe_allow_html=True)

##### CREER DES TAB 
tab1, tab2, tab3, tab4, tab5 = st.tabs(['PRÉSENTATION','EXPÉRIENCES', 'SOFTSKILLS', 'HARDSKILLS', 'FORMATIONS'])


###############################################################################################################################################
##### Presentation

with tab1:
    
     # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    # crea de div
    main_container1 = st.container()

    info_cont, sep_cont1, photo_cont, sep2, info2_cont = main_container1.columns([2, 1, 2, 1, 2])
    
   
        
    with info_cont:
        
        # Ajouter espaces
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # textes
        st.markdown('<p style=" font-family: Kalam; font-size:40px;text-align: center;">Anthony Iervasi</p>', unsafe_allow_html=True)
        
        # Ajouter espaces
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        st.markdown('<p style=" font-family: Kalam; font-size: 23px;text-align: center;">&#11088; 30 Ans <br> &#x1F3E0; Aix Les Bains <br> &#x1F4F1; +33 7 67 97 18 42 <br> &#x1F4EB; anthodev69@gmail.com </p>', unsafe_allow_html=True)
        
    with photo_cont:
        
        # affichage photo
        st.image(photo, use_column_width=True)
        
    with info2_cont:
        
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        
        # textes
        st.markdown('<p style=" font-family: Kalam; font-size:30px;">Langues</p>', unsafe_allow_html=True)
        
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">&#x1F1EB;&#x1F1F7; Langue Maternelle <br> &#x1F1EC;&#x1F1E7; Niveau B2  </p>', unsafe_allow_html=True)
        
        # Ajouter espaces
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        
        # logo github avec lien
        link = "https://github.com/anthoiervasi73"
        image_url = "https://images.squarespace-cdn.com/content/v1/5eac4ca67214b127262c77be/1590166986407-YQZV8HIAPRL41D7EAXKM/github-logo.jpg"
        html_code = f'<a href="{link}" target="_blank"><img src="{image_url}" alt="Image" style="width: 200px;"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        
         # logo linkedin avec lien
        link = "https://www.linkedin.com/in/anthony-iervasi/"
        image_url = "https://logos-marques.com/wp-content/uploads/2021/03/logo-Linkedin.jpg"
        html_code = f'<a href="{link}" target="_blank"><img src="{image_url}" alt="Image" style="width: 200px;"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        
    


###############################################################################################################################################
##### Experiences

with tab2:
    
     # crea de div
    main_container2 = st.container()

    chart_cont2, sep_container2, info_cont2 = main_container2.columns([4, 2, 4])
    
    with chart_cont2:
        
       
        
        # data XP pour barplot horizontal
        data_xp = {'Postes' : ['Technicien de maintenance informatique', 'Carreleur', 'Développeur Web & Mobile', 'Responsable Réception & Stock',
                                'Développeur Wordpress', 'Data Analyst - BI Analyst'],
                   'XP' : [1,4,0.5,1,3,0.5],
                   'Prise de poste' : ['2014','2015','2019','2019','2020','2023'],
                   'Type de poste' : ['CDD','Auto-entreprise','Stage','CDI','Auto-entreprise','Stage']}

        # crea du df
        df_xp = pd.DataFrame(data_xp)

        # Ordonner les postes par ordre croissant
        ordered_postes = df_xp['Postes'].unique().tolist()

        # Crea du graphique à barres horizontal avec Plotly Express
        xp = px.bar(df_xp, x='XP', y='Postes', color='Type de poste', orientation='h',
                   color_discrete_map={
                                        "Auto-entreprise": "#B5DEFF",
                                        "Stage": "#F7C8E0",
                                        "CDD": "#DDFFBB",
                                        "CDI": "#A267AC"})



        xp.update_layout(

                        plot_bgcolor='white',
                        width=750,
                        height=650,
                        yaxis=dict(title='Postes',
                                   showline=True,
                                   categoryorder='array',
                                   categoryarray=ordered_postes),

                        xaxis=dict(title="Années d'expérience",
                                  gridcolor='Lightgrey'))

        # Afficher le graphique
        st.plotly_chart(xp)
        
        
    with info_cont2:
        
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        
        # textes
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">2023 - Data Analyst - BI Analyst :</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">- Réalisation d\'analyses data, et business intelligence <br> - Réalisation de Dataviz au travers de Dashboard ou de web-app <br> - Création d\'algorithmes prédictifs et de recommandations grâce au machine Learning </p>', unsafe_allow_html=True)
        
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">2020 - Développeur Wordpress : </p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">- Comptabilité, Réalisation de devis, Gestion de projet, Relation client <br> - Réalisation de sites clefs en main avec Elementor, Gestion de l\'hébergement</p>', unsafe_allow_html=True)
       
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">2019 - Responsable Réception & Stock : </p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">- Gestion d\'équipe, planning <br> - Réception physique et informatique de la marchandise, Gestion des stocks <br> - Implantation complète des produits dans l\'entrepôt dans un but d\'optimisation des chemins de préparation commandes</p>', unsafe_allow_html=True)
       
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">2019 - Développeur Web & Mobile : </p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">- Projet client : Réalisation d\'un mvp pour une application cross-plateform d\'aide aux malvoyants avec Angular & Ionic en méthode agile Scrum : <a href="https://vocaleo-app.com/">vocaleo-app</a> <br> - Projet Ecole : Développement d’un jeu 2d type Bomberman avec javascript en méthode agile Scrum</p>', unsafe_allow_html=True)
        
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">2015 - Carreleur : </p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">- Comptabilité, Réalisation de devis, Gestion de chantier, Relation client <br> - Pose de carrelage sol et faïence, Jointage</p>', unsafe_allow_html=True)
        
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">2014 - Technicien de maintenance informatique : </p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">- Hotline, Prise en compte des demandes utilisateurs, Résolution et prise en main à distance, Gestion des interventions sur site <br> - Technicien Hardware, Software, Réseau, Dépannage logiciel, Matériel & Montage / Préparation de PC en atelier et installation sur site</p>', unsafe_allow_html=True)

    
    
    
###############################################################################################################################################
##### Softskills 

with tab3:
    # creation de div
    main_container3 = st.container()

    chart_cont3, sep_container3, info_cont3 = main_container3.columns([4, 2, 4])
    
    with chart_cont3:
        # data softskills pour donuts chart
        data_soft = {'Softskills' : ['Autonomie','Perseverance','Exigeance','Force de Proposition'],
                     '%_Soft' : [25,25,25,25] }

        # creation du df
        df_soft = pd.DataFrame(data_soft)

        # Définir les valeurs, les noms et les couleurs
        values = df_soft['%_Soft']
        names = df_soft['Softskills']
        colors = ['#B5DEFF', '#F7C8E0', '#DDFFBB', '#A267AC']

        # Créer le graphique circulaire (pie chart)
        soft = go.Figure(data=[go.Pie(labels=names, values=values, hole=0.5,
                                    marker=dict(colors=colors))])
        soft.update_traces(textposition='inside', textinfo='label')
        soft.update_layout(showlegend=False,width=800, height=700)

        # Afficher le graphique
        st.plotly_chart(soft)
    
    with info_cont3:
        
        # Ajouter plusieurs espaces
        st.markdown("<br>", unsafe_allow_html=True)
        
        # textes
        
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">Autonomie :</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">Grâce aux diverses activités que j\'ai effectuées en auto-entreprise, je suis devenu parfaitement autonome pour réaliser toutes les taches qui me sont confiées. <br>  J\'ai également débuté la programmation en autodidacte et j\'ai gardé l\'habitude d\'effectuer une veille régulière, ce qui me permet de me perfectionner sur les technos que j\'utilise mais également de m\'autoformer rapidement sur d\'éventuelles nouvelles technologies qui pourront m\'être utile pour mon métier d\'analyste</p>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">Persévérance :</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">Mes parcours professionnel et personnel m\'ont appris que dans chaque situation il est possible de faire face à des difficultés diverses et variées. <br> C\'est grâce à ma persévérance et à ma capacité à rester positif que je réussis en tout temps à surmonter les épreuves, afin de mener à bien les missions qui me sont confiées.</p>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">Exigence :</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">Mon amour du travail bien fait m\'a mené à développer une certaine exigence envers moi même mais également envers mes collaborateurs. <br> Couplé à ma bienveillance naturelle, cela me permet de motiver positivement mon équipe afin de fournir des rendus toujours plus aboutis et professionnels.</p>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        ###
        st.markdown('<p style=" font-family: Kalam; font-size: 17px;">Force de Proposition :</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Roboto; font-size: 13px;">Au travers des projets que j\'ai réalisé grâce à mes activités d\'entrepreneur, j\'ai acquis un talent certain en matière de réflexion et de proposition, ce qui ma permis d\'accompagner mes clients dans la réalisation de leurs projets en les conseillant et en leur proposant des alternatives et améliorations diverses.<br>Cela me permettra également d\'aider ma future équipe de manière pertinente sur les phases de réflexion projet. </p>', unsafe_allow_html=True)
        
        


    
###############################################################################################################################################    
##### HArdskills 

with tab4:
    
        # data hardskills pour barplot
        data_hard = {'Hardskills' : ['Excel','SQL','MySQL','Python','Numpy','Pandas','Microsoft Power BI','Tableau Software','Matplotlib','Seaborn','Plotly',
                                'Scikit-Learn','Streamlit','Wordpress','HTML','CSS','Javascript','Git-GitHub','Shell','C'],
                 'XP' : [1,1,1,2,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,3,1.5,1.5,1,3,1,1],
                 'Catégories' : ['Traitement des Données','Traitement des Données','Traitement des Données','Traitement des Données',
                               'Traitement des Données','Traitement des Données','DataViz','DataViz','DataViz','DataViz','DataViz',
                                'Machine Learning','Web','Web','Web','Web','Web','Divers','Divers','Divers'] }

        # crea du df
        df_hard = pd.DataFrame(data_hard)

        #graph

        hard = px.bar(df_hard, x='Hardskills', y='XP', color='Catégories',
                  color_discrete_map={
                                    "Traitement des Données": "#B5DEFF",
                                    "DataViz": "#F7C8E0",
                                    "Machine Learning": "#ECA869",
                                    "Web": "#DDFFBB",
                                    "Divers": "#A267AC"})

        hard.update_yaxes(title='Années d\'expérience', dtick=0.5)


        hard.update_layout(
            width=1350,
            height=500,
            plot_bgcolor='white',
            yaxis = dict( 
                    mirror=True,
                    ticks='outside',
                    showline=True,
                    gridcolor='gainsboro')) 

         # Afficher le graphique
        st.plotly_chart(hard)
        

    
###############################################################################################################################################
##### Formation 

with tab5:
    
    # Ajouter plusieurs espaces
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # creation de div
    main_container5 = st.container()

    img_cont1, sep1, text_cont1, sep2, img_cont2, sep3, text_cont2 = main_container5.columns([2,1,2,1,2,1,2])
    
    
    
    with img_cont1:
        
        # affichage logo
        st.image(image, use_column_width=True)
        
        
    with text_cont1:
        
        #texte
        
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">2023</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">Formation Data Analyste</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">Equivalence de niveau 6</p>', unsafe_allow_html=True)
        
    with sep2:
        
        # separateur vertical
        st.markdown("""<div style="height: 100px; border-left: 2px solid lightgrey; margin: 0 0 0 40px;"></div>""", unsafe_allow_html=True)
        
        
    with img_cont2:
        
        # affichage logo
        st.image(image, use_column_width=True)
        
        
    with text_cont2:
        
        #texte
        
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">2019</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">Formation Développeur web</p>', unsafe_allow_html=True)
        st.markdown('<p style=" font-family: Kalam; font-size: 18px;">Equivalence de niveau 5</p>', unsafe_allow_html=True)
        
