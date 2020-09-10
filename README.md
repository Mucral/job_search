# Recherche d'emploi
Application Web permettant d'avoir' les dernières offres d'emplois.

## Exigence
- Python >= 3.8
    - BeautifulSoup4 >= 4.9.*
    - Requests >= 2.24.*
    - Django == 3.1

## Installation

###Linux

```
dnf install vim python3.8 git screen firewalld
git clone https://github.com/Florian-Dj/job_search.git
cd jobs_search
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
chmod ug+x run.sh
```
Si vous avez installé firewalld
```
firewall-cmd --zone=public --add-port=8000/tcp --permanent
firewall-cmd --reload
```

## Utilisation
```
cd job_search
./run.sh
```
Vous pouvez vous lancer votre navigateur web avec l'url ip:8000

## Mise à jour
**V0.3**
- Pannel Web Django
- Pannel Admin
- Page Accueil avec les statistiques des annonces
- Page pour voir les recherche et annonces
- Formulaire pour ajouter des recherches
- Logo *(supprimer et modifier)* les recherches
- Ajout de filtres pour annonces  *(Tout, Non Lu, Postulé, Expiré, Inadéquate)*
- Ajout de filtres pour annonces *(Leboncoin, Linkedin, Pole-Emploi)*
- Bouton pour chercher les nouvelles annonces
- Changer les status des annonces sur la page admin

V0.2
- Ajout du status des annonces *(non lues, postulées, inadéquite, expirées)*
- Ajout un sous menu dans les annonces *(non lue, postulée, expirée, inadéquate)*
- Possibilité de voir toutes les annonces du même status d'un site
- Ajout d'une  colonne status dans la table annonce

## Idées
- Ajouter d'autres site de recherche
- Identifier les annonces déjà expirées
- Mettre les annonces en inadéquate suivant des mots clef
- Savoir si l'annonce est relancée *(redondante pour negocier le salaire)*
