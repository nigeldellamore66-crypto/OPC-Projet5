	Script de migration Python d'un fichier healthcare_dataset.csv vers une base MongoDB


	1. Fonctionnement

Le script charge le fichier CSV dans un DataFrame Pandas.

Les données sont nettoyées / normalisées (formatage du nom, arrondi du prix).

Le DataFrame est converti en liste de dictionnaires (records).

Les enregistrements sont insérés dans la collection patients de la base healthcare.

Le script peut utiliser une variable d’environnement MONGO_URI si elle est définie, sinon il utilise une valeur par défaut.

	2. Configuration

Le script lit l’URI MongoDB ainsi :

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")

	Option 1 : utiliser la valeur par défaut

Si Mongo tourne en conteneur mongo, aucune config n’est nécessaire.

	Option 2 : définir la variable d'environnement
	
			Sous Linux / Mac :
export MONGO_URI="mongodb://localhost:27017/healthcare"

			Sous Windows (PowerShell) :
setx MONGO_URI "mongodb://localhost:27017/healthcare"

		Dans Docker Compose :
services:
  migration:
    environment:
      - MONGO_URI=mongodb://mongo:27017/healthcare

	3. Exécution
python migrate.py


Résultat attendu :

Connexion à MongoDB : OK
Import de X patients terminé 

	4.Vérification des données

		Dans Mongo shell :

use healthcare
db.patients.countDocuments()


Pour afficher quelques patients :

db.patients.find().limit(5).pretty()

	5.Dépendances
	
pandas:	  Lecture CSV

pymongo:	Connexion et insertion dans MongoDB

Installer les dépendances :

pip install pandas pymongo
