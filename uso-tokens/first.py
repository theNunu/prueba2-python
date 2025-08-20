import jwt
import datetime
import time

# --- Paso 1: Configuración de la clave secreta ---
# Esta clave es solo para el servidor. Nunca la compartas.
SECRET_KEY = "mi_clave_secreta_super_segura"

# --- Paso 2: Crear el token ---
# Se crea un 'payload' (carga útil) con la información que deseas almacenar.
# Incluimos la fecha de expiración ('exp') para que el token no sea válido para siempre.
payload = {
    'user_id': 123,
    'username': 'juan_perez',
    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=2)
}

print("imprimiendo el payload: ")
print(payload)
# Se codifica (firma) el payload con la clave secreta.
# El algoritmo 'HS256' es el más común para firmas simétricas.
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("Token JWT generado:")
print(token)
print("-" * 20)

# --- Paso 3: Decodificar y verificar el token ---
# Esto simula lo que haría el servidor al recibir una solicitud.
print("Verificando el token...")

try:
    # Intenta decodificar el token usando la misma clave secreta.
    # Si la firma no coincide o el token ha expirado, lanzará un error.
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    
    print("✅ ¡Token válido!")
    print("Payload decodificado:")
    print(decoded_payload)

except jwt.ExpiredSignatureError:
    print("❌ Error: El token ha expirado.")

except jwt.InvalidTokenError:
    print("❌ Error: El token no es válido o la firma es incorrecta.")