from main import llamar_todos_datos

print("Obteniendo datos de la base de datos...")

try:
    # Llama a la función que devuelve los productos
    productos = llamar_todos_datos()

    # Recorre y muestra los productos obtenidos
    for producto in productos:
        print(producto)

except sqlite3.OperationalError as e:
    print(f"Error al obtener los datos: {e}")