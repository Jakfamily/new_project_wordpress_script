import os
import requests
import shutil
import webbrowser

def create_wordpress_project(project_name):
    # Définir le chemin du projet dans le répertoire WAMP
    project_path = os.path.join("C:\\wamp64\\www", project_name)

    # Créer le dossier du projet
    os.makedirs(project_path, exist_ok=True)

    # Télécharger la dernière version de WordPress
    wordpress_url = "https://wordpress.org/latest.zip"
    response = requests.get(wordpress_url)

    # Enregistrer le fichier zip dans le dossier du projet
    zip_path = os.path.join(project_path, "wordpress.zip")
    with open(zip_path, "wb") as f:
        f.write(response.content)

    # Extraire le contenu du fichier zip dans le dossier du projet
    shutil.unpack_archive(zip_path, project_path)

    # Récupérer le chemin du dossier "wordpress" extrait
    wordpress_dir = os.path.join(project_path, "wordpress")

    # Parcourir tous les fichiers et dossiers dans le dossier "wordpress"
    for item in os.listdir(wordpress_dir):
        # Déplacer chaque fichier ou dossier à la racine du projet
        shutil.move(os.path.join(wordpress_dir, item), project_path)

    # Supprimer le dossier "wordpress" vide
    os.rmdir(wordpress_dir)

    # Supprimer le fichier zip
    os.remove(zip_path)

    # Ouvrir le projet dans Google Chrome
    url = f"http://localhost/{project_name}"
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)

if __name__ == "__main__":
    project_name = input("Entrez le nom du projet WordPress : ")
    create_wordpress_project(project_name)
    print("Projet WordPress créé avec succès !")
