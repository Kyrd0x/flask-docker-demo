from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

# La route principale renvoie index.html
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Le formulaire fait un POST vers /infos
@app.route("/infos", methods=["POST"])
def infos():
    # On récupère le fichier
    file = request.files.get("file")
    file_info = None
    # Si le fichier existe, on calcule sa taille et on formate la date
    if file and file.filename:
        # Calcul de la taille du fichier
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0)

        # Formattage de la date
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # On crée un objet avec les infos du fichier
        file_info = {
            "name": file.filename,
            "size": size,
            "time": time
        }
    return render_template("infos.html", file_info=file_info)

if __name__ == "__main__":
    # On lance le serveur Flask sur le port 5000, ouvert à l'extérieur
    app.run(host="0.0.0.0", port=5000)
