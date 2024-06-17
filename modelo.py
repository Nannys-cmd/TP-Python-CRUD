import sqlite3

# Función para conectar a la base de datos
def conectar():
    conn = sqlite3.connect('db/estudiantes.db')
    return conn

# Función para crear la tabla 'estudiantes' si no existe
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un estudiante a la base de datos
def agregar_estudiante(nombre, edad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    conn.close()

# Función para listar todos los estudiantes
def listar_estudiantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estudiantes')
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes

# Función para obtener un estudiante por su ID
def obtener_estudiante(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estudiantes WHERE id = ?', (id,))
    estudiante = cursor.fetchone()
    conn.close()
    return estudiante

# Función para actualizar un estudiante por su ID
def actualizar_estudiante(id, nombre, edad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE estudiantes SET nombre = ?, edad = ? WHERE id = ?', (nombre, edad, id))
    conn.commit()
    conn.close()

# Función para eliminar un estudiante por su ID
def eliminar_estudiante(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM estudiantes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
