# JEFERSON REYES
# EJERCICIO5|P2

n = int(input("Introduce la altura deseada: "))

# Bucle

for i in range(1, n + 1):
    # BUCLE 2
    for j in range(2 * i -1, 0, -2):
        print(j, end= " ")
    print(" ")