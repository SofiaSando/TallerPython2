'''Calcule el promedio de goles anotados por un jugador en cuatro encuentros, solo 
si la suma de estos es mayor a 10; de lo contrario imprimir “No se puede determinar 
el promedio”.
'''

partido1=float(input("Ingrese los goles del primer encuentro: "))
partido2=float(input("Ingrese los goles del segundo encuentro: "))
partido3=float(input("Ingrese los goles del tercer encuentro: "))
partido4=float(input("Ingrese los goles del cuarto encuentro: "))
golesTotales=partido1+partido2+partido3+partido4
if golesTotales >10 :
    promedio=golesTotales/4
    print(f"El promedio de los goles anotados en los cuatro encuentros es de: {promedio}")
else :
    print(f"No se puede determinar el promedio")
