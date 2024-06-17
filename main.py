import tkinter as tk
from vista import CRUDApp
from modelo import crear_tabla

if __name__ == '__main__':
    crear_tabla()  # Asegura que la tabla estudiantes exista al inicio
    root = tk.Tk()
    root.title('CRUD de Estudiantes')
    app = CRUDApp(root)
    root.mainloop()
