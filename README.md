Script de migration Python d'un fichier healthcare_dataset.csv vers une base MongoDB


1. Fonctionnement
   

- Le script commence par créer un utilisateur "healthcare_app" avec le mot de passe "password123" qui sera utilisé pour accéder à MongoDB.

- Le fichier CSV est chargé dans un DataFrame Pandas.

- Les données sont nettoyées / normalisées (formatage du nom, arrondi du prix).

- Le DataFrame est converti en liste de dictionnaires (records).

- Les enregistrements sont insérés dans la collection patients de la base healthcare.

- Le script peut utiliser une variable d’environnement MONGO_URI si elle est définie, sinon il utilise une valeur par défaut.


2. Configuration
   
Le script lit l’URI MongoDB ainsi :

	MONGO_URI = os.getenv("MONGO_URI", "mongodb://healthcare_app:password123@mongo:27017/healthcare?authSource=healthcare")

- Option 1 : utiliser la valeur par défaut

Si Mongo tourne en conteneur mongo, aucune config n’est nécessaire.

- Option 2 : définir la variable d'environnement:
	
Sous Linux / Mac :

	export MONGO_URI="mongodb://healthcare_app:password123@mongo:27017/healthcare?authSource=healthcare"

Sous Windows (PowerShell) :

	setx MONGO_URI "mongodb://healthcare_app:password123@mongo:27017/healthcare?authSource=healthcare"

Dans Docker Compose :

	services:
  	migration:
    	environment:
      	- MONGO_URI=mongodb://healthcare_app:password123@mongo:27017/healthcare?authSource=healthcare


3. Exécution


		python migrate.py


4. Résultat attendu :


		Utilisateur healthcare_app créé

		55500 enregistrements insérés dans healthcare.patients


6. Vérification des données


Dans Mongo shell :

	use healthcare

	db.auth("healthcare_app", "password123")
	
	db.patients.countDocuments()

	db.patients.find().limit(5).pretty()


6. Dépendances

	
	pandas:	  Lecture CSV

	pymongo:	Connexion et insertion dans MongoDB

Installer les dépendances :

	pip install pandas pymongo
	
