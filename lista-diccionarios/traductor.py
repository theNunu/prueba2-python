# Crea un diccionario con palabras en español y sus traducciones en inglés
traductor = {
    'hola': 'hello', #clave: valor
    'adios': 'goodbye',  #clave: valor
    'perro': 'dog',    #clave: valor
    'gato': 'cat',  #clave: valor
    'casa': 'house' #clave: valor
}
print(traductor)
dato = traductor.get('perro')
print(dato)
print(f'la palabra {traductor.get('perro')} se traduce como {dato}')

# Pide al usuario que ingrese una palabra en español
palabra_espanol = input("Ingresa una palabra para traducir (hola, adios, perro, gato, casa): ").lower()

# Verifica si la palabra ingresada existe como clave en el diccionario
if palabra_espanol in traductor:
    # Si la palabra existe, obtiene su traducción (el valor)
    traduccion = traductor[palabra_espanol]
    print(f"La traducción de '{palabra_espanol}' es '{traduccion}'.")
else:
    # Si la palabra no está en el diccionario, muestra un mensaje de error
    print(f"Lo siento, la palabra '{palabra_espanol}' no se encuentra en el diccionario.")

