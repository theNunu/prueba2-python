from hasheo import hashear_contrasena, hacer_login

contrasena = input("ingresa una contraseña: ")

contrasena_hasheada = hashear_contrasena(contrasena)

print(f"Contraseña original: {contrasena}")
print(f"contraseña con Hash SHA-256 es : {contrasena_hasheada}")



# Imprimir el resultado
hacer_login(contrasena_hasheada)


