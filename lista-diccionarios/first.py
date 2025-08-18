# Creando un diccionario para un usuario
usuario = {
    'nombre': 'Juan', # clave única y un valor.
    'edad': 30,   # clave única y un valor. 
    'ciudad': 'Madrid' # clave única y un valor.
}

print(usuario)
# Acceder a un valor usando su clave
print(f"El nombre del usuario es: {usuario['nombre']}") # Salida: El nombre del usuario es: Juan
print(f"La edad del usuario es: {usuario.get('edad')}")  # Otra forma de acceder, más segura.

# Intentar acceder a una clave que no existe da un error
# print(usuario['pais'])  # ¡Esto daría un KeyError!
# La función .get() evita el error y devuelve None si la clave no existe
print(usuario.get('pais')) # Salida: None
# print(usuario['pais'])

# Añadir un nuevo par clave-valor
usuario['ciudad'] = 'Barcelona'
print(usuario) # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Barcelona'}


# Modificar un valor existente
usuario['edad'] = 31
print(usuario) # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Barcelona'}