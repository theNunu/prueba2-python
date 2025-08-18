import hashlib
user = input("ingresa un usuario: ")
password = input("ingresa una contraseña: ")


password_bytes = password.encode("utf-8")
print(password_bytes)

sha256 = hashlib.sha256()
print(f"el sha256 es:  {sha256}")

# actualizar el objeto hash con los datos
sha256.update(password_bytes)
print(f"hash actualizado con sha256: {password_bytes}")

#  Obtener el valor hash en formato hexadecimal
hash_contrasena = sha256.hexdigest()

# Imprimir el resultado
print(f"Contraseña original: {password}")
print(f"Hash SHA-256: {hash_contrasena}")