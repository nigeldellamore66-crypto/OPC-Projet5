import pandas as pd
from pymongo import MongoClient
import os

# Connexion à la base healthcare en root
root_uri = "mongodb://admin:admin123@mongo:27017/admin"
client = MongoClient(root_uri)
db = client['healthcare']
username = "healthcare_app"
userpwd = "password123"

# Création de l'utilisateur pour l'app
try:
    db.command("createUser", username,
               pwd=userpwd,
               roles=[{"role": "readWrite", "db": "healthcare"}])
    print("Utilisateur healthcare_app créé")
except Exception as e:
    print("Erreur:", e)
    
# Connexion à MongoDB (hostname vient de docker-compose)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://healthcare_app:password123@mongo:27017/healthcare?authSource=healthcare")
DB_NAME = os.getenv("MONGO_DB", "healthcare")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "patients")

# Chargement du CSV
df = pd.read_csv("healthcare_dataset.csv")

# Nettoyage léger : normaliser les noms et arrondir le montant
df["Name"] = df["Name"].str.title().str.strip()
df["Billing Amount"] = df["Billing Amount"].round(2)

# Connexion à MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Insertion des données
records = df.to_dict(orient="records")
collection.insert_many(records)

print(f"{len(records)} enregistrements insérés dans {DB_NAME}.{COLLECTION_NAME}")
