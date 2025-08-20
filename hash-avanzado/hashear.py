def hashear_password(password):
    
    password_hasheada = password.encode("utf-8")
    
    import hashlib
    sha256  = hashlib.sha256()
    sha256.update(password_hasheada)
    
    ready_password = sha256.hexdigest()
    
    return ready_password

def doing_register(password):

    # nombre = input("ingrese un nombre: ")
    password_register_hashed= hashear_password(password)

    print(f"""
    la contraseña original es : {password}
    tu contraseña haheada es: {password_register_hashed}
    """)
    return password_register_hashed

def doing_login():
    print("\n****  ***  HAGAMOS EL LOGIN ***   ****")
    password_to_compare = input("recuerdas tu contraseña?: ")
    password_login_hashed = hashear_password(password_to_compare)
    return password_login_hashed


def descodificar_contrasena(password):
    result = doing_register(password)
    import jwt
    password_deshaheada = jwt.decode(result,algorithms=["HS256"])

    return password_deshaheada

    
# def comparar_hashes(password_login_hashed, password_register_hashed)-> bool:
#     #comparar contraseñas de login y register hasheadas
#     password_login = doing_login(password_login_hashed)
#     password_register = doing_register(password_register_hashed)
#     if password_login == password_register:
#         print("las contraseñas hasheadas SI COINCIDEN")
#         return True
#     else:
#         print("no coinciden")
#     return False

# # La lógica principal del programa
# if __name__ == "__main__":
#     # --- Paso 1: Registro del usuario ---
#     print("Iniciando el proceso de registro...")
#     contrasena_registrada_hash = doing_register()

#     # --- Paso 2: Bucle de login ---
#     # Usamos un bucle `while True` para pedir la contraseña hasta que sea correcta
#     while True:
#         # Obtenemos el hash de la contraseña ingresada en el login
#         contrasena_ingresada_hash = doing_login()
        
#         # --- Paso 3: Comparación de hashes ---
#         if contrasena_ingresada_hash == contrasena_registrada_hash:
#             print("\n✅ ¡Éxito! Las contraseñas hasheadas COINCIDEN.")
#             print("El programa se detendrá.")
#             break  # Salimos del bucle si la contraseña es correcta
#         else:
#             print("\n❌ ¡Error! Las contraseñas hasheadas NO COINCIDEN.")
#             print("Inténtalo de nuevo.")

