import datetime

# --- Paso 1: Usar timedelta para sumar días ---

# Crea un objeto `timedelta` para representar una duración de 7 días.
una_semana = datetime.timedelta(days=7)
print(una_semana)
# Obtiene la fecha actual.
hoy = datetime.date.today()
print(f"Hoy es: {hoy}")

# Suma el `timedelta` a la fecha actual para obtener la fecha de la próxima semana.
proxima_semana = hoy + una_semana
print(f"La próxima semana será: {proxima_semana}")

# --- Paso 2: Calcular la diferencia entre dos fechas ---

# Define la fecha actual con la hora incluida.
now = datetime.datetime.now()

# Define una fecha en el pasado.
fecha_pasada = datetime.datetime(2024, 1, 1)

# Calcula la diferencia entre las dos fechas. El resultado es un objeto `timedelta`.
diferencia = now - fecha_pasada

# Imprime la diferencia en días.
print(f"Han pasado {diferencia.days} días desde el 1 de enero de 2024.")