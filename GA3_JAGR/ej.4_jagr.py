# JAGR
# Simulacion de carga de servidores

# Mostramos un titulo descriptivo para nuestro programa
print(" ")
print(" >>> PROGRAMA 4: CARGA DE SERVIDORES (anidado) <<< ")

# Solicitamos al usuario la cantidad de servidores que desea simular
# input() captura la entrada del usuario como texto, int() lo convierte a numero entero
servidores = int(input("> ¿Cuantos servidores desea simular?: "))

# Solicitamos al usurio la cantidad de procesos por cada servidor
procesos = int(input("> ¿Cuantos procesos por servidor?: "))

# Iniciamos un bucle for para recorrer cada servidor, desde 1 hasta la cantidad indicada
for i in range(1, servidores + 1):

    # Mostramos el numero del servidor actual
    print(" ")
    print(f"> Servidor #{i}: ")

    # Iniciamos un segundo bucle (anidado) para los procesos de cada servidor
    # Este bucle se ejecuta completo por cada iteracion del bucle exterior (cada servidor)
    for j in range(1, procesos + 1):
        # Mostramos un mensaje que indica que el proceso se esta cargando
        # Usamos sangria en el print para mostrar jerarquia visual
        print(f"  Cargando proceso {j}...")