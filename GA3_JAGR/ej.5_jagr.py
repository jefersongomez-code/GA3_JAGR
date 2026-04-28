# JAGR
# Visualizacion de puestos por departamento

# Mostramos un titulo para identificar el programa
print(" ")
print(" >>> PROGRAMA 5: PUESTOS POR DEPARTAMENTO (anidado) <<< ")
# Solicitamos al usuario la cantidad total de departamentos a ingresar
# input() devuelve una cadena, asi que usamos int() para convertirlo a numeor entero
departamentos = int(input("> ¿Cuantos departamento hay?: "))
# Creamos una lista vacia donde almacenaremos los nombres de los departamentos
nombre_departamentos = []
# Iniciamos un bucle for que se repite una vez por cada departamento
for i in range(departamentos):

    # Solicitamos el nombre del departamento actual
    # Mostramos el numero usando (i + 1) porque range empieza desde 0
    nombre = input(f"> Nombre del departamento #{i +1}: ")

    # Agregamos el nombre del departamento a la lista creada anteriormente
    nombre_departamentos.append(nombre)

    # Solicitamos al usuario cuantos puestos hay dentro de este departamento
    puestos = int(input(f"> ¿Cuantos puestos tiene {nombre}?: "))

    # Mostramos un subtitulo antes de listar los puestos del departamento
    print(" ")
    print(f"> Puestos en {nombre}: ")