from config import db

def crear_usuario(nombre, correo):
    # Crear un nuevo documento con ID automático
    doc_ref = db.collection('usuarios').document()
    doc_ref.set({
        'nombre': nombre,
        'correo': correo
    })
    print(f"\n✅ Usuario creado con ID: {doc_ref.id}")

# === Entrada por consola ===
if __name__ == "__main__":
    print("=== Crear nuevo usuario ===")
    
    nombre = input("📝 Ingresa el nombre del usuario: ")
    correo = input("📧 Ingresa el correo del usuario: ")

    crear_usuario(nombre, correo)
