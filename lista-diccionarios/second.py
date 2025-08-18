calificaciones = {
    'Matemáticas': 9,  #clave: valor
    'Ciencias': 8,    #clave: valor
    'Historia': 7    #clave: valor
}

print(calificaciones)
cal = calificaciones.get('Historia')
print(cal)

print('   ----   (clave): calificaciones   ----- ')
for calificacion in calificaciones:
    print(calificacion)

print("   -----  Valores (Calificaciones):  ---- ")
for calificacion in calificaciones.values():
    print(calificacion)
# Salida:
# 9
# 8
# 7

print('usando doble recorrido .items()')
print("""  
    Se le llama así porque el bucle for está desempaquetando (asignando) dos elementos a la vez:
    el primer elemento de cada tupla a la variable asignatura y el segundo a la variable calificacion.
    Esta sintaxis es muy potente y te permite acceder a ambos datos en cada paso del bucle.

""")

for asignatura, calificion in calificaciones.items():
    print(asignatura, calificacion)

for asig in calificaciones.items():
    print(asig)