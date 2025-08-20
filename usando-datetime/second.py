import datetime


# Crea una fecha y hora para el 1 de enero de 2025 a las 10:30 AM
fecha_especifica = datetime.datetime(2025, 8, 9, 9, 0, 0)
print(f"mi cumpleaños: {fecha_especifica}")


fecha_actual = datetime.date(2025, 8, 9)
print(f"fecha actual: {fecha_actual}")
dia_actual = fecha_actual.weekday()
print(dia_actual)


def evaluar_dia_match(dia_actual):
    match dia_actual:
        case 0:
            return "Lunes"
        case 1:
            return "Martes"
        case 2:
            return "Miércoles"
        case 3:
            return "Jueves"
        case 4:
            return "Viernes"
        case 5:
            return "Sábado"
        case 6:
            return "Domingo"
        case _:
            return "Día inválido"


print(evaluar_dia_match(dia_actual))  # Imprime: Martes
