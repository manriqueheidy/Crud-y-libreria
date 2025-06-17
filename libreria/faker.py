from faker import Faker

fake = Faker('es_CO')  # Para datos más realistas en Colombia

def generar_usuarios(cantidad):
    usuarios = []
    for _ in range(cantidad):
        usuario = {
            "nombre": fake.name(),
            "direccion": fake.address(),
            "correo": fake.email(),
            "telefono": fake.phone_number(),
            "empresa": fake.company(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=65),
            "documento": fake.random_number(digits=10, fix_len=True)
        }
        usuarios.append(usuario)
    return usuarios

# Generar y mostrar 5 usuarios falsos
usuarios_falsos = generar_usuarios(5)

for i, u in enumerate(usuarios_falsos, 1):
    print(f"\nUsuario {i}")
    for clave, valor in u.items():
        print(f"{clave.capitalize()}: {valor}")