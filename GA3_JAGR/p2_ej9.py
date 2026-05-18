# JEFERSON REYES
# EJERCICIO5|P2
import pyfiglet

titulo = pyfiglet.figlet_format("Jeferson")
print(titulo)

pc = "Contraseña"
inten = ""
while inten != pc:inten = input("Introduce la contraseña: ")
if inten != pc:
    print("ERROR! Intentalo de nuevo")
else:
    print("\u001b[35mContraseña Correcta")