# JAGR
# Simulacion de errores en logs

# Mostramos un titulo descriptivo para que el usuario sepa que hace el programa
print(" ")
print(" >>> PROGRAMA 3: SIMULACION DE LOGS DE ERROR <<< ")

# Solicitamos al usuario cuantos errores desea simular
# Utilizamos input() para capturar el dato y lo convertimos a entero con int()
errores = int(input("> ¿Cuantos errores desea simular?: "))

# Iniciamos un bucle for que se repetira desde 1 hasta el ingresado por el usuario
# range(1, errores + 1) genera una secuencia del 1 al numero indicado (inclusive)
for i in range(1, errores + 1):
    # En cada iteracion se imprime un mensaje de error simulado con el numero de error
    # Utilizamos f-string para ionsertar dinamicamente el valor de 'i' en el texto
    print(f"[ERROR {i}] Fallo detectado en el sistema de base de datos.")