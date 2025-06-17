from config import db

def actualizar_usuario(doc_id, nuevos_datos):
    doc_ref = db.collection('usuarios').document(doc_id)
    doc_ref.update(nuevos_datos)
    print(f"\n✅ Usuario con ID {doc_id} actualizado.")

if __name__ == "__main__":
    print("=== Actualizar usuario existente ===")

    doc_id = input("🆔 Ingresa el ID del usuario a actualizar: ")
    nuevo_nombre = input("📝 Nuevo nombre: ")
    nuevo_correo = input("📧 Nuevo correo: ")

    try:
        actualizar_usuario(doc_id, {
            "nombre": nuevo_nombre,
            "correo": nuevo_correo
        })
    except Exception as e:
        print(f"❌ Error: {e}")
