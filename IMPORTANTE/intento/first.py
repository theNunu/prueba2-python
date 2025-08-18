import sys
texto = """ 
    este es un texto
    de prueba para esa porqueria,
    para que pueda entender como se usa esa nota
"""
def procesar_texto(texto):
    """
    Convierte el texto a mayúsculas y lo imprime.
    """
    print(texto.upper())

if __name__ == '__main__':
    # Comprobamos si hay al menos un argumento en la línea de comandos
    # El primer elemento de sys.argv (sys.argv[0]) es siempre el nombre del script
    if len(sys.argv) > 1:
        # sys.argv[1] es el primer argumento que el usuario introduce
        texto_a_procesar = sys.argv[1]
        procesar_texto(texto_a_procesar)
    else:
        print("Por favor, proporciona un texto como argumento. Ejemplo: python procesador.py 'hola mundo'")