# JAGR
# Registro de asistencia

print(" ")
print(" >>> PROGRAMA 1: REGISTRO DE ASISTENCIA <<< ")
# Pedimos la cantidad de empleados
total_empleados = int(input("> Ingrese el numero de empleados a registrar: "))
# Inicializamos el contador
contador = 0
# Lista para almacenar los nombres
asistencia = []

# Inicia el bucle While
while contador < total_empleados:
    # Solicitamos el nombre
    nombre = input(f"> Ingrese el nombre del empleado #{contador + 1}: ")

    # Agregamos a la lista
    asistencia.append(nombre)

    # Confirmacion de registro
    print(f"{nombre} ha sido registrado.")

    # Incrementamos el contador
    contador += 1

# Mostramos los empleados registrados
print(" ")
print("> Listado Completo: ")
for persona in asistencia:
    print("- ", persona)
