import hashlib

def hashear_contrasena(contrasena):

    contrasena_bytes = contrasena.encode("utf-8")

    hash256 = hashlib.sha224()

    hash256.update(contrasena_bytes)


    has_contrasena = hash256.hexdigest()

    

    return has_contrasena


def hacer_login(contrasena_hasheada):
    while True:

        print("\n******Hagamos el login*****")
        contrasena_acordada = input("recuerdas la contraseña?: ")
        contrasena_a_comparar = hashear_contrasena(contrasena_acordada)

        if contrasena_a_comparar == contrasena_hasheada:
            print(f"""\n
            SON IGUALES
            el ingreso funciono ya que la contraseña hasheada inicialmente es: {contrasena_hasheada}
            y la contraseña que acabas de ingresar para comparar las contraseña es: {contrasena_a_comparar}

                                                
            """)
            False
            break #para romper el ciclo
        else:
            print("la contraseña no es igual, intentalo otra vez")


