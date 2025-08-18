import sqlite3
from pathlib import Path
BD = Path("manejo-database")

conexion = sqlite3.connect(BD /"champeon.db" )
cur = conexion.cursor()

def configurar_base_de_datos():
    """
    Crea la tabla 'product' si no existe.
    """
    # Usamos 'IF NOT EXISTS' para evitar el error si la tabla ya existe
    cur.execute("CREATE TABLE IF NOT EXISTS champeon(id, name, rol, life)")
    conexion.commit()

def insertar_datos_iniciales():
    """
    Inserta datos iniciales en la tabla.
    """
    cur.execute("""
        INSERT INTO champeon VALUES
        (1, 'garen', 'top', 200),
        (2, 'nunu', 'jungla', 150),
        (3, 'jinx', 'adc', 80),
        (4, 'serafine', 'soporte', 100)
    """)
    conexion.commit()
    print("Datos iniciales insertados.")

def llamar_todos_datos():
    """
    Obtiene y devuelve todos los datos de la tabla 'product'.
    """
    cur.execute("SELECT * FROM  champeon")
    return cur.fetchall()

# Llama a las funciones de configuración e inserción una vez que el archivo se ejecuta directamente
if __name__ == '__main__':
    configurar_base_de_datos()
    # Si quieres insertar los datos iniciales, descomenta la siguiente línea:
    # insertar_datos_iniciales()
    print("Base de datos configurada.")