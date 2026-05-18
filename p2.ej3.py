# JEFERSON REYES
# EJERCICIO3|P2

n = int(input("\u001b[36mIntroduce un numero entero positivo: "))

for i in range(1, n + 1, 2):
    if i >= n - 1:
        print("Numeros impares desde 0 hasta ", i)
    else:
        print(i, end=", ")