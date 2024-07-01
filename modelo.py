import sqlite3

def crear_conexion(db_file):
    try:
        conexion = sqlite3.connect(db_file)
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tablas(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Productos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                Descripcion TEXT,
                Precio REAL,
                Categoria_ID INTEGER,
                Proveedor_ID INTEGER,
                FOREIGN KEY (Categoria_ID) REFERENCES Categorias (ID),
                FOREIGN KEY (Proveedor_ID) REFERENCES Proveedores (ID)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categorias (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                Descripcion TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Proveedores (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                Direccion TEXT,
                Telefono TEXT
            )
        """)
        
        conexion.commit()
        print("Tablas creadas exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al crear las tablas: {e}")

def crear_producto(conexion, nombre, descripcion, precio, categoria_id, proveedor_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Productos (Nombre, Descripcion, Precio, Categoria_ID, Proveedor_ID)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, precio, categoria_id, proveedor_id))
        
        conexion.commit()
        print("Producto creado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al crear el producto: {e}")

def ver_todos_los_productos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Productos")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener los productos: {e}")
        return []

def ver_producto_por_id(conexion, producto_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Productos WHERE ID = ?", (producto_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al obtener el producto: {e}")
        return None

def actualizar_producto(conexion, producto_id, nombre, descripcion, precio, categoria_id, proveedor_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Productos
            SET Nombre = ?, Descripcion = ?, Precio = ?, Categoria_ID = ?, Proveedor_ID = ?
            WHERE ID = ?
        """, (nombre, descripcion, precio, categoria_id, proveedor_id, producto_id))
        
        conexion.commit()
        print("Producto actualizado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")

def eliminar_producto(conexion, producto_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Productos WHERE ID = ?", (producto_id,))
        
        conexion.commit()
        print("Producto eliminado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")

# CRUD functions for categories
def crear_categoria(conexion, nombre, descripcion):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Categorias (Nombre, Descripcion)
            VALUES (?, ?)
        """, (nombre, descripcion))
        
        conexion.commit()
        print("Categoría creada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la categoría: {e}")

def ver_todas_las_categorias(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Categorias")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener las categorías: {e}")
        return []

def ver_categoria_por_id(conexion, categoria_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Categorias WHERE ID = ?", (categoria_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al obtener la categoría: {e}")
        return None

def actualizar_categoria(conexion, categoria_id, nombre, descripcion):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Categorias
            SET Nombre = ?, Descripcion = ?
            WHERE ID = ?
        """, (nombre, descripcion, categoria_id))
        
        conexion.commit()
        print("Categoría actualizada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar la categoría: {e}")

def eliminar_categoria(conexion, categoria_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Categorias WHERE ID = ?", (categoria_id,))
        
        conexion.commit()
        print("Categoría eliminada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar la categoría: {e}")

# CRUD functions for suppliers
def crear_proveedor(conexion, nombre, direccion, telefono):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Proveedores (Nombre, Direccion, Telefono)
            VALUES (?, ?, ?)
        """, (nombre, direccion, telefono))
        
        conexion.commit()
        print("Proveedor creado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al crear el proveedor: {e}")

def ver_todos_los_proveedores(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Proveedores")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener los proveedores: {e}")
        return []

def ver_proveedor_por_id(conexion, proveedor_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Proveedores WHERE ID = ?", (proveedor_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al obtener el proveedor: {e}")
        return None

def actualizar_proveedor(conexion, proveedor_id, nombre, direccion, telefono):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Proveedores
            SET Nombre = ?, Direccion = ?, Telefono = ?
            WHERE ID = ?
        """, (nombre, direccion, telefono, proveedor_id))
        
        conexion.commit()
        print("Proveedor actualizado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar el proveedor: {e}")

def eliminar_proveedor(conexion, proveedor_id):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Proveedores WHERE ID = ?", (proveedor_id,))
        
        conexion.commit()
        print("Proveedor eliminado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar el proveedor: {e}")
