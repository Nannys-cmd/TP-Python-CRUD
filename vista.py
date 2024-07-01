from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import modelo

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario")
        self.root.configure(bg='#f0f0f0')
        self.conexion = modelo.crear_conexion("tienda_ropa.db")
        modelo.crear_tablas(self.conexion)

        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self.root, bg='#f0f0f0')
        self.frame.pack(padx=10, pady=10)

        self.label_nombre = Label(self.frame, text="Nombre:", bg='#f0f0f0', font=('Arial', 12))
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nombre = Entry(self.frame, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        self.label_descripcion = Label(self.frame, text="Descripción:", bg='#f0f0f0', font=('Arial', 12))
        self.label_descripcion.grid(row=1, column=0, padx=5, pady=5)

        self.entry_descripcion = Entry(self.frame, font=('Arial', 12))
        self.entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        self.label_precio = Label(self.frame, text="Precio:", bg='#f0f0f0', font=('Arial', 12))
        self.label_precio.grid(row=2, column=0, padx=5, pady=5)

        self.entry_precio = Entry(self.frame, font=('Arial', 12))
        self.entry_precio.grid(row=2, column=1, padx=5, pady=5)

        self.label_categoria_id = Label(self.frame, text="Categoría ID:", bg='#f0f0f0', font=('Arial', 12))
        self.label_categoria_id.grid(row=3, column=0, padx=5, pady=5)

        self.entry_categoria_id = Entry(self.frame, font=('Arial', 12))
        self.entry_categoria_id.grid(row=3, column=1, padx=5, pady=5)

        self.label_proveedor_id = Label(self.frame, text="Proveedor ID:", bg='#f0f0f0', font=('Arial', 12))
        self.label_proveedor_id.grid(row=4, column=0, padx=5, pady=5)

        self.entry_proveedor_id = Entry(self.frame, font=('Arial', 12))
        self.entry_proveedor_id.grid(row=4, column=1, padx=5, pady=5)

        self.boton_crear = Button(self.frame, text="Crear Producto", command=self.crear_producto, bg='#4caf50', fg='white', font=('Arial', 12, 'bold'))
        self.boton_crear.grid(row=5, column=0, columnspan=2, pady=10)

        self.boton_ver_todos = Button(self.frame, text="Ver Todos los Productos", command=self.ver_todos_los_productos, bg='#2196f3', fg='white', font=('Arial', 12, 'bold'))
        self.boton_ver_todos.grid(row=6, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Descripción", "Precio", "Categoría ID", "Proveedor ID"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Categoría ID", text="Categoría ID")
        self.tree.heading("Proveedor ID", text="Proveedor ID")
        self.tree.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        self.tree.bind("<Double-1>", self.on_tree_select)

        self.boton_actualizar = Button(self.frame, text="Actualizar Producto", command=self.actualizar_producto, bg='#ff9800', fg='white', font=('Arial', 12, 'bold'))
        self.boton_actualizar.grid(row=8, column=0, columnspan=2, pady=10)

        self.boton_eliminar = Button(self.frame, text="Eliminar Producto", command=self.eliminar_producto, bg='#f44336', fg='white', font=('Arial', 12, 'bold'))
        self.boton_eliminar.grid(row=9, column=0, columnspan=2, pady=10)

    def crear_producto(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        precio = float(self.entry_precio.get())
        categoria_id = int(self.entry_categoria_id.get())
        proveedor_id = int(self.entry_proveedor_id.get())
        
        modelo.crear_producto(self.conexion, nombre, descripcion, precio, categoria_id, proveedor_id)
        messagebox.showinfo("Éxito", "Producto creado exitosamente.")
        self.ver_todos_los_productos()

    def ver_todos_los_productos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        productos = modelo.ver_todos_los_productos(self.conexion)
        if productos:
            for producto in productos:
                self.tree.insert("", "end", values=producto)
        else:
            print("No hay productos en la base de datos.")

    def on_tree_select(self, event):
        item = self.tree.selection()[0]
        producto = self.tree.item(item, "values")
        self.entry_nombre.delete(0, END)
        self.entry_nombre.insert(0, producto[1])
        self.entry_descripcion.delete(0, END)
        self.entry_descripcion.insert(0, producto[2])
        self.entry_precio.delete(0, END)
        self.entry_precio.insert(0, producto[3])
        self.entry_categoria_id.delete(0, END)
        self.entry_categoria_id.insert(0, producto[4])
        self.entry_proveedor_id.delete(0, END)
        self.entry_proveedor_id.insert(0, producto[5])
        self.selected_product_id = producto[0]

    def actualizar_producto(self):
        if hasattr(self, 'selected_product_id'):
            producto_id = self.selected_product_id
            nombre = self.entry_nombre.get()
            descripcion = self.entry_descripcion.get()
            precio = float(self.entry_precio.get())
            categoria_id = int(self.entry_categoria_id.get())
            proveedor_id = int(self.entry_proveedor_id.get())
            
            modelo.actualizar_producto(self.conexion, producto_id, nombre, descripcion, precio, categoria_id, proveedor_id)
            messagebox.showinfo("Éxito", "Producto actualizado exitosamente.")
            self.ver_todos_los_productos()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un producto para actualizar.")

    def eliminar_producto(self):
        if hasattr(self, 'selected_product_id'):
            producto_id = self.selected_product_id
            modelo.eliminar_producto(self.conexion, producto_id)
            messagebox.showinfo("Éxito", "Producto eliminado exitosamente.")
            self.ver_todos_los_productos()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")
