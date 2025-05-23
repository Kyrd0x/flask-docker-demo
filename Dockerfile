# Image minimaliste : Debian + Python
FROM python:3.10-slim

# Définir le dossier de travail dans le container 
WORKDIR /app

# Copier les fichiers du projet dans le container 
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5000

# Définir la variable d’environnement FLASK_APP   
ENV FLASK_APP=app.py

# Lancer l’application Flask
CMD ["python", "app.py"]