import tkinter as tk
from tkinter import ttk
from modelo import agregar_estudiante, actualizar_estudiante, eliminar_estudiante, listar_estudiantes

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title('CRUD de Estudiantes')

        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.label_nombre = ttk.Label(self.frame, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry_nombre = ttk.Entry(self.frame, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.label_edad = ttk.Label(self.frame, text="Edad:")
        self.label_edad.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_edad = ttk.Entry(self.frame, width=10)
        self.entry_edad.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.btn_agregar = ttk.Button(self.frame, text="Agregar", command=self.agregar_estudiante)
        self.btn_agregar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.btn_actualizar = ttk.Button(self.frame, text="Actualizar", command=self.actualizar_estudiante)
        self.btn_actualizar.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.btn_eliminar = ttk.Button(self.frame, text="Eliminar", command=self.eliminar_estudiante)
        self.btn_eliminar.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        self.tabla_estudiantes = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Edad"), show="headings")
        self.tabla_estudiantes.heading("ID", text="ID")
        self.tabla_estudiantes.heading("Nombre", text="Nombre")
        self.tabla_estudiantes.heading("Edad", text="Edad")
        self.tabla_estudiantes.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.cargar_tabla()

    def cargar_tabla(self):
        estudiantes = listar_estudiantes()
        self.tabla_estudiantes.delete(*self.tabla_estudiantes.get_children())
        for estudiante in estudiantes:
            self.tabla_estudiantes.insert("", "end", values=estudiante)

    def agregar_estudiante(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        agregar_estudiante(nombre, edad)
        self.cargar_tabla()
        self.limpiar_campos()

    def actualizar_estudiante(self):
        item = self.tabla_estudiantes.selection()
        if item:
            id = self.tabla_estudiantes.item(item, "values")[0]
            nombre = self.entry_nombre.get()
            edad = self.entry_edad.get()
            actualizar_estudiante(id, nombre, edad)
            self.cargar_tabla()
            self.limpiar_campos()

    def eliminar_estudiante(self):
        item = self.tabla_estudiantes.selection()
        if item:
            id = self.tabla_estudiantes.item(item, "values")[0]
            eliminar_estudiante(id)
            self.cargar_tabla()
            self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
