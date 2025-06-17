from config import db

def eliminar_usuario(doc_id):
    doc_ref = db.collection('usuarios').document(doc_id)
    doc_ref.delete()
    print(f"\n🗑️ Usuario con ID {doc_id} eliminado.")

# Entrada por consola
if __name__ == "__main__":
    print("=== Eliminar usuario ===")
    doc_id = input("🆔 Ingresa el ID del usuario a eliminar: ")

    try:
        eliminar_usuario(doc_id)
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")
