inventario: dict = {
    'agua': 8,
    'azucar': 5,
    'mayonesa': 3,
    'papel': 4
}
print(inventario)
# for invent in inventario.values():
#     print(invent)
# print(inventario)
# for producto, cantidad in inventario.items():
#     print(f'{producto}  le quedan: {cantidad}')




def mostar_productos_restantes(inventario=dict, cantidad_producto=int):
    for producto, cantidad in inventario.items():
        if producto == producto_tienda:
            cantidad_restante =  cantidad - cantidad_producto 
            print(f'perfecto, del producto {producto_tienda} queda : {cantidad_restante}')
            
            # Añadir un nuevo par clave-valor
            inventario[producto] = cantidad_restante # actualisar los valores(clave, valor)
            print('lo que queda en total: ' , inventario)
    

def quitar_productos(inventario=dict):
    if producto_tienda in inventario:
        print(f'el producto {producto_tienda} si existe')
        cantidad_producto = int(input(f'cuanto quieres del producto {producto_tienda}?: '))
        # print(cantidad_producto)
        if cantidad_producto > inventario.get(producto_tienda):
            print('la cantidad que quieres es mayor a la cantidad de nuestro inventario')
        else:
            mostar_productos_restantes(inventario, cantidad_producto)

            

    else:
        print(f'el producto {producto_tienda} NO existe')

producto_tienda = input('cual producto quieres?: ').lower()

quitar_productos(inventario)