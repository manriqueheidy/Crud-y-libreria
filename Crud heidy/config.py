import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa Firebase solo una vez
cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()
