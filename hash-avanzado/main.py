from hashear import doing_login, doing_register, descodificar_contrasena

password = input("Ingrese una contraseña: ")
def main():
      print("Iniciando el proceso de registro...")

      contrasena_registrada_hash = doing_register(password)

      # --- Paso 2: Bucle de login ---
      # Usamos un bucle `while True` para pedir la contraseña hasta que sea correcta
      while True:
            # Obtenemos el hash de la contraseña ingresada en el login
            contrasena_ingresada_hash = doing_login()

            # --- Paso 3: Comparación de hashes ---
            if contrasena_ingresada_hash == contrasena_registrada_hash:
                  print("El programa se detendrá.")
                  print("\n✅ ¡Éxito! Las contraseñas hasheadas COINCIDEN.")

                  # print("DESCODIFICANDO LA LA CONTRASEÑA DE REGISTER")
                  # contrasena_descodificada = descodificar_contrasena(contrasena_registrada_hash)
                  # print(contrasena_descodificada)

                  break  # Salimos del bucle si la contraseña es correcta
            else:
                  print("\n❌ ¡Error! Las contraseñas hasheadas NO COINCIDEN.")


main()