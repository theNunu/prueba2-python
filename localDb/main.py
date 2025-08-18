import sqlite3

# CARPETA = 'local.db/'
conexion= sqlite3.connect("localDb/producto.db")

cur = conexion.cursor() # con cursor se ejecutan sentencias SQL y se obtienen resultados de consultas SQL,

cur.execute("CREATE TABLE product(id, name, quantity)")

res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
('product')

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
True


"""  
Ahora, agregue dos filas de datos suministrados como literales
SQL ejecutando una declaración, una vez más llamando a :INSERT

"""
cur.execute("""
    INSERT INTO product VALUES
        (1, 'aceite la favorita', 35),
        (2, 'fosforo', 200),
        (3, 'mayonesa maggi', 55),
        (4, 'cachitos', 23)
""")

"""
La instrucción abre implícitamente una transacción, que debe confirmarse antes de que 
los cambios se guarden en la base de datos 
Llamada al objeto de conexión Para confirmar la transacción:INSERT

"""

conexion.commit()

res = cur.execute("SELECT name FROM product")
print(res)
res.fetchall()
[('fosforo',), ('cachitos',)]
print(res)

# Ahora, inserte tres filas más llamando a :

data = [
    (5, "pulp", 23),# 1 objeto con 3 atributos
    (6, "coca cola", 30), # 2 objeto con 3 atributos
    (7, "atun bancam", 12), # 3 objeto con 3 atributos
]
cur.executemany("INSERT INTO product VALUES(?, ?, ?)", data)
conexion.commit()  # Remember to commit the transaction after executing INSERT.
datos_mostrar = cur


def llamar_todos_datos():
    """
    Obtiene y devuelve todos los datos de la tabla 'product'.
    """
    cur.execute("SELECT * FROM product")
    return cur.fetchall()
