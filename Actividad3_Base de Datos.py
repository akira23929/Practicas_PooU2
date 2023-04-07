import sqlite3

# Crear una conexión con la base de datos
conn = sqlite3.connect('example.db')

# Crear una tabla en la base de datos
conn.execute('''CREATE TABLE usuarios
                 (id INTEGER PRIMARY KEY,
                  nombre TEXT NOT NULL,
                  edad INTEGER);''')

# Insertar datos en la tabla
conn.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 25))
conn.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('María', 32))
conn.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Pedro', 19))

# Consultar los datos de la tabla
cursor = conn.execute("SELECT id, nombre, edad FROM usuarios")
for row in cursor:
    print("ID = ", row[0])
    print("Nombre = ", row[1])
    print("Edad = ", row[2], "\n")

# Actualizar datos en la tabla
conn.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (25, 'Juan'))

# Eliminar datos de la tabla
conn.execute("DELETE FROM usuarios WHERE nombre = 'Pedro'")

# Cerrar la conexión con la base de datos
conn.close()

