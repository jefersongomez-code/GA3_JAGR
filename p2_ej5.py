# JEFERSON REYES
# EJERCICIO5|P2

c = int(input("Ingrese la cantidad que desea invertir: "))
i_a = int(input("¿Cual es el interes anual?: "))
a = int(input("¿Por cuantos años: "))

i = i_a/100

# Condicion

for i in range(1,a + 1):
    montof = c*(1+i)**a
    print(f"En este año se genero {montof}")