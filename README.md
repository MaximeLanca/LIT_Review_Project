# LIT_Review_Project

Ce dépôt contient une application Django.  
Ce guide détaille comment installer, configurer et lancer le projet en local — que ce soit pour du développement, des tests ou de la contribution.

# 1. Prérequis
Avant de commencer, installer :
- **Python 3.10+**
- **Git**
- (Optionnel) **VS Code / PyCharm**

# 2. Cloner le dépôt
- **git clone https://github.com/MaximeLanca/LIT_Review_Project.git**
- **cd LIT_Review_Project**

# 3. Environnement virtuell
Créer un environnement Python isolé : python -m venv env
Activation de l'environnement: (Windows) env\Scripts\Activate.ps1, (macOS/Linux) source env/bin/activate

# 4. Installer les dépendances
- **pip install --upgrade pip**
- **pip install -r requirements.txt**

# 5. Lancer le serveur local
python manage.py runserver

Accès: 
- **Application : http://127.0.0.1:8000/**
- **Interface admin : http://127.0.0.1:8000/admin/**