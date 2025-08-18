import hashlib

# 1. Definir la entrada (la contraseña en este caso)
contrasena = "mi_clave_secreta"

# 2. Codificar la entrada a bytes
# El algoritmo hash necesita que la entrada sea en formato de bytes.
# 'utf-8' es el estándar para codificar texto.
contrasena_bytes = contrasena.encode('utf-8')

# 3. Crear un objeto hash usando el algoritmo deseado (SHA-256)
sha256 = hashlib.sha256()

# 4. Actualizar el objeto hash con los datos
sha256.update(contrasena_bytes)

# 5. Obtener el valor hash en formato hexadecimal
hash_contrasena = sha256.hexdigest()

# 6. Imprimir el resultado
print(f"Contraseña original: {contrasena}")
print(f"Hash SHA-256: {hash_contrasena}")

# --- Verificación ---
# Si intentas hashear la misma contraseña de nuevo, obtendrás el mismo hash.
sha256_2 = hashlib.sha256()
sha256_2.update("mi_clave_secreta".encode('utf-8'))
print(f"\nVerificación (mismo hash): {sha256_2.hexdigest()}")