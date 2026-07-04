# HACKER UNION AI

HACKER UNION AI est un script Python pour Termux qui analyse l’appareil, affiche des informations système et propose des profils de jeu pour BGMI et Free Fire.

## Fonctionnalités:

- Analyse BGMI.
- Analyse Free Fire.
- Analyse du stockage.
- Booster de performance.
- Informations appareil.
- Recommandations FPS.
- Analyse batterie et température.

## Prérequis:

Avant de lancer le script, installe :

- Termux.
- Python.
- Git.
- Termux:API.
- Le paquet `termux-api` dans Termux.

## Installation:

```bash
pkg update && pkg upgrade -y
pkg install git python termux-api -y
git clone https://github.com/housseini1960/hacker-union-ai.git
cd hacker-union-ai
python main.py

Utilisation:

Une fois le programme lancé :
.Choisis 1 pour BGMI.
.Choisis 2 pour Free Fire.
.Choisis 3 pour l’analyse du stockage.
.Choisis 4 pour le booster.
.Choisis 5 pour voir les informations du projet.
.Choisis 6 pour quitter.

Notes:

Le script utilise des commandes Android/Termux comme getprop, settings, et termux-battery-status.
Certaines fonctions peuvent dépendre des autorisations Android et de Termux:API.
Le script doit être exécuté dans Termux sur Android.

Dépannage:

Si le programme refuse de démarrer :
.Vérifie que Python est bien installé.
.Vérifie que le fichier principal s’appelle bien main.py.
.Vérifie que Termux:API est installé.
.Vérifie qu’aucune ligne n’a été cassée lors du copier-coller.
