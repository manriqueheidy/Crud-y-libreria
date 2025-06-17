from config import db

def leer_usuarios():
    usuarios = db.collection('usuarios').stream()
    for usuario in usuarios:
        print(f"{usuario.id} => {usuario.to_dict()}")

# Prueba
leer_usuarios()
