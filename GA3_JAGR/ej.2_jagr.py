# JAGR
# Listado de Tareas

# Mostramos un titulo para el programa
print(" ")
print(" >>> PROGRAMA 2: REGISTRO DE TAREAS <<< ")
# Solicitamos al usuario cuantas tareas quiere ingrear
# Usamos int() para convertir la entrada de texto a numero entero
cantidad = int(input("> ¿Cuantas tareas deseas ingresar?: "))
# Creamos una lista vacia llamada 'tareas' para almacenar los nombres de las tareas
tareas = []
# Iniciamos un bucle for que se repite desde 0 hasta (cantidad - 1)
for i in range(cantidad):
    # Mostramos el numero de tarea que se va a ingresar (usamos 1 + 1 para que empiece desde 1)
    # y solicitamos al usuario el nombre de la tarea
    tarea = input(f"> Ingrese la tarea #{i + 1}: ")

    # Agregamos (append) la tarea a la lista de tareas
    tareas.append(tarea)

# Mostramos un mensaje indicando que vamos a imprimir todas las tareas ingresadas
print(" ")
print("> Tareas Registradas: ")
# Usamos otro bucle for para recorrer e imprimir las tareas ya guardadas en la lista
# len(tareas) devuelve la cantidad total de tareas ingresadas
for i in range(len(tareas)):
    # Imprimimos la tarea con su numero correspondiente (1 + 1) y el contenido de la tarea
    print(f"> Tarea {i + 1}: {tareas[i]}")