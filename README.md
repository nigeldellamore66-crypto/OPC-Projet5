Script de migration Python d'un fichier healthcare_dataset.csv vers une base MongoDB


1. Fonctionnement
   

- Le script commence par créer un utilisateur "healthcare_app" avec le mot de passe "password123" qui sera utilisé pour accéder à MongoDB.

- Le fichier CSV est chargé dans un DataFrame Pandas.

- Les données sont nettoyées / normalisées (formatage du nom, arrondi du prix).

- Le DataFrame est converti en liste de dictionnaires (records).

- Les enregistrements sont insérés dans la collection patients de la base healthcare.

- Le script peut utiliser une variable d’environnement MONGO_URI si elle est définie, sinon il utilise une valeur par défaut.


2. Configuration

- Option 1 : utiliser les valeurs par défaut

Par défaut la connexion est configurée avec l'utilisateur "healthcare_app", le mot de passe "password123", la base de donnée "healthcare", et la collection "patients".

- Option 2 : modifier les variables de configuration et définir la variable d'environnement:

Modifier le nom d'utilisateur et le mot de passe à créer dans MongoDB :

	username = "healthcare_app"
	userpwd = "password123"

Modifier les paramètres de connexion à la base de donnée:

	MONGO_URI = os.getenv("MONGO_URI", "mongodb://healthcare_app:password123@mongo:27017/healthcare?authSource=healthcare")
	DB_NAME = os.getenv("MONGO_DB", "healthcare")
	COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "patients")

La variable d'environnement peut également être définie en dehors du script :
	
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


5. Résultat attendu :

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
	
