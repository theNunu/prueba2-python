"""
date: Almacena solo una fecha (año, mes, día).

time: Almacena solo una hora (hora, minuto, segundo, microsegundo).

datetime: Almacena tanto la fecha como la hora.

timedelta: Representa una duración o la diferencia entre dos fechas, horas o datetime.

"""

import datetime

print("imprimir fecha y hora actual:  ")
hora_y_fecha_actual = datetime.datetime.now()

print(f"la hora actual es: {hora_y_fecha_actual}")

print("\n")
print("imprimir solo la fecha actual:")
fecha_actual = datetime.date.today()

print(f"fecha actual: {fecha_actual}")

otra_fecha_actual = datetime.date.weekday(fecha_actual) -1

print(f"otra_fecha_hora_actual: {otra_fecha_actual}")


now = datetime.datetime.now()
# Solo la hora actual
current_time = now.time()
print(f"Hora actual: {current_time}")