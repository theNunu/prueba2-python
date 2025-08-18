
nombre = input("ingrese un nombre: ")
password = input("Ingrese una contraseña: ")
    
from hashear import hashear_password
    
respuesta = hashear_password(password)

print(f"""
      hola {nombre}
      tu contraseña haheada es: {respuesta}
      
      
      """)
    
   