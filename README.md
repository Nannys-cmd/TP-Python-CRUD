# CRUD de Estudiantes en Python con Tkinter y SQLite

Este proyecto implementa un CRUD (Crear, Leer, Actualizar, Eliminar) básico para gestionar estudiantes utilizando Python con Tkinter para la interfaz gráfica y SQLite como base de datos relacional.

## Requisitos

- Python 3.x instalado (preferiblemente Python 3.6+)
- Biblioteca estándar de Python: `tkinter` (generalmente incluida con Python)
- SQLite 3 (generalmente incluido con Python)

## Instalación y Configuración

1. **Clonar el repositorio:**

git clone https://github.com/tu_usuario/crud_estudiantes.git
cd crud_estudiantes


2. **Instalar dependencias (si es necesario):**

No se requieren dependencias externas más allá de las bibliotecas estándar de Python para este proyecto.

3. **Ejecutar la aplicación:**

Para iniciar la aplicación, ejecuta `main.py`:

python main.py


## Funcionalidades

- **Agregar Estudiante:** Permite ingresar el nombre y edad de un estudiante y agregarlo a la base de datos.
- **Actualizar Estudiante:** Actualiza el nombre y edad de un estudiante existente seleccionado desde una tabla.
- **Eliminar Estudiante:** Elimina un estudiante seleccionado desde una tabla.
- **Listar Estudiantes:** Muestra todos los estudiantes almacenados en la base de datos en una tabla.

## Estructura del Proyecto

crud_estudiantes/
│
├── db/
│ └── estudiantes.db # Archivo de base de datos SQLite
│
├── modelo.py # Funciones para interactuar con la base de datos
├── vista.py # Interfaz de usuario usando Tkinter
├── main.py # Punto de entrada principal de la aplicación
└── README.md # Documentación del proyecto (este archivo)

## Equipo de Trabajo:
- Daniela Bastias (danybastias@outlook.com)
- Abel (-----@---.com)
- Karem Lisbeth Nuñez Rivera (nuezr.karemclases@gmail.com)

## Contribución

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request. Cualquier sugerencia, corrección o mejora es bienvenida.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
