# gestor-tareas-python
Gestor de tareas pendientes en consola desarrollado en Python. Permite listar, agregar, marcar tareas como completadas y contar pendientes mediante recursividad.

Gestor de Tareas Pendientes (CLI en Python)

Aplicación de consola desarrollada en **Python** para organizar y administrar tareas pendientes de forma rápida y sencilla. Ideal para practicar estructuras de datos (listas y diccionarios), manejo de excepciones y funciones recursivas.

Funcionalidades

- **Ver tareas:** Muestra todas las tareas numeradas con su estado actual (`[ ]` pendiente o `[X]` completada).
- **Agregar tareas:** Permite registrar nuevas tareas validando que la descripción no quede vacía.
- **Marcar como completada:** Actualiza el estado de una tarea según su posición, con manejo de errores (`ValueError` e `IndexError`) ante entradas inválidas.
- **Conteo recursivo:** Calcula el total de tareas pendientes utilizando una función recursiva (`contar_tareas_pendientes`).

 Requisitos

- Python 3.x instalado en el sistema.

Cómo ejecutarlo

1. Clona este repositorio o descarga el archivo `mi_gestor_tareas.py`.
2. Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
# En Windows
py mi_gestor_tareas.py

# En Linux / macOS
python3 mi_gestor_tareas.py
