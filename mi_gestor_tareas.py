def obtener_tareas():
    """Inicializa y retorna una lista de tareas de ejemplo.

    No recibe parámetros.
    Retorna una lista de diccionarios con las llaves "descripcion" (str)
    y "completada" (bool) para cada tarea.
    """
    tareas = [
        {
            "descripcion": "Estudiar programación",
            "completada": False
        },
        {
            "descripcion": "Hacer ejercicios de algebra lineal",
            "completada": True
        },
        {
            "descripcion": "Hacer autoevaluacion de algoritmos",
            "completada": False
        }
    ]

    return tareas


def mostrar_tareas(lista_tareas):
    """Muestra todas las tareas numeradas y su estado.

    Parámetro:
        lista_tareas: Lista de tareas que se desea mostrar.

    No retorna ningún valor.
    """
    print("\n--- LISTA DE TAREAS ---")

    # enumerate con start=1 para que la numeración empiece en 1
    for i, tarea in enumerate(lista_tareas, start=1):
        if tarea["completada"]:
            estado = "[X]"
        else:
            estado = "[ ]"

        print(f"{i}. {estado} {tarea['descripcion']}")


def agregar_tarea(lista_tareas, descripcion):
    """Agrega una nueva tarea a la lista.

    Parámetros:
        lista_tareas: Lista donde se agregará la tarea.
        descripcion: Texto que describe la nueva tarea.

    Retorna:
        La lista de tareas modificada.
    """
    # toda tarea nueva empieza como pendiente
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False
    }

    lista_tareas.append(nueva_tarea)

    return lista_tareas


def marcar_completada(lista_tareas, posicion):
    """Marca una tarea como completada.

    Parámetros:
        lista_tareas: Lista de tareas.
        posicion: Número de posición de la tarea (inicia en 1).

    No retorna ningún valor.
    Maneja el error si la posición no existe.
    """
    try:
        # con 0 o negativos no daría error en Python, así que los saco aquí
        if posicion < 1:
            raise IndexError

        # le resto 1 porque el usuario cuenta desde 1 y la lista desde 0
        lista_tareas[posicion - 1]["completada"] = True

        print("¡Tarea marcada como completada!")

    except IndexError:
        print("Error: La posición ingresada no existe.")


def contar_tareas_pendientes(lista_tareas, indice=0):
    """Cuenta recursivamente las tareas que están pendientes.

    Parámetros:
        lista_tareas: Lista de tareas que se desea revisar.
        indice: Posición actual de la recursión (inicia en 0).

    Retorna:
        Un número entero con el total de tareas pendientes.
    """

    # caso base: ya revisé todas las tareas, no queda nada por contar
    if indice == len(lista_tareas):
        return 0

    # caso recursivo: si la tarea está pendiente sumo 1 y sigo con la siguiente
    if not lista_tareas[indice]["completada"]:
        return 1 + contar_tareas_pendientes(lista_tareas, indice + 1)

    else:
        # si ya está completada no sumo nada, solo paso a la siguiente
        return contar_tareas_pendientes(lista_tareas, indice + 1)


# programa principal
tareas = obtener_tareas()

# el menú se repite hasta que el usuario elige salir
while True:
    print("\n--- GESTOR DE TAREAS PENDIENTES ---")
    print("1. Ver todas las tareas")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Mostrar total de tareas pendientes")
    print("5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        mostrar_tareas(tareas)

    elif opcion == "2":
        descripcion = input("Describe la nueva tarea: ")

        # no dejo agregar tareas vacías
        if descripcion.strip():
            tareas = agregar_tarea(tareas, descripcion)
            print("¡Tarea agregada!")
        else:
            print("Error: La descripción no puede estar vacía.")

    elif opcion == "3":
        # el ValueError salta si escriben algo que no es un número
        try:
            posicion = int(input("Número de la tarea a marcar como completada: "))
            marcar_completada(tareas, posicion)

        except ValueError:
            print("Error: Debes ingresar un número entero.")

    elif opcion == "4":
        total = contar_tareas_pendientes(tareas)
        print(f"Total de tareas pendientes: {total}")

    elif opcion == "5":
        print("¡Gracias por utilizar el gestor de tareas!")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")
