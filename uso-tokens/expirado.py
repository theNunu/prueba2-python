import jwt
import datetime
import time

# --- Configuración de la clave secreta ---
SECRET_KEY = "mi_clave_secreta_super_segura"

# --- Paso 1: Crear un token que ya ha expirado ---
# Le restamos 60 minutos a la hora actual, por lo que expiró en el pasado.
payload_expirado = {
    'user_id': 456,
    'username': 'ana_lopez',
    'exp': datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=60)
}

token_expirado = jwt.encode(payload_expirado, SECRET_KEY, algorithm="HS256")

print("Token JWT expirado generado:")
print(token_expirado)
print("-" * 20)

# --- Paso 2: Intentar verificar el token ---
# El servidor intentaría decodificarlo.
print("Intentando decodificar el token expirado...")

try:
    decoded_payload = jwt.decode(token_expirado, SECRET_KEY, algorithms=["HS256"])
    
    print("✅ ¡Token válido!")
    print("Payload decodificado:", decoded_payload)

except jwt.ExpiredSignatureError:
    # Este es el error esperado
    print("❌ ¡Error! El token ha expirado. Necesitas iniciar sesión de nuevo.")

except jwt.InvalidTokenError:
    # Este error se lanzaría si la firma fuera incorrecta
    print("❌ Error: El token no es válido o la firma es incorrecta.")