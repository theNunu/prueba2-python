print("""   
                                -----ARGS------  ES UNA TUPLA
    podemos definir funciones genéricas que no aceptan un número 
    determinado de parámetros, sino que se “adaptan” al número de argumentos 
    con los que son llamados.

""")

def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

suma_total = suma(1, 3, 4, 2)
print(suma_total) #Salida 10


suma_total = suma(1, 1) #Salida 2
print(suma_total)



def suma2(*args):
    return sum(args)

suma_total = suma2(2,3,9)
print(suma_total) # 14
