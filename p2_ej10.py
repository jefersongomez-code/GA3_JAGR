# JEFERSON REYES
# EJERCICIO5|P2
import pyfiglet

titulo = pyfiglet.figlet_format("Jeferson")
print(titulo)

word = input("Introduce una palabra: ")
# Recorremos desde el indice final hasta el 0
for i in range(len(word) - 1, -1, -1):
    print("\u001b[36m", word[i])