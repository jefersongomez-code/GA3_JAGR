# JEFERSON REYES
# EJERCICIO5|P2
import pyfiglet

titulo = pyfiglet.figlet_format("Jeferson")
print(titulo)

while True:
    entrada = input("Escribe algo (escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    print(entrada)