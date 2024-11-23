'''Desarrolle un algoritmo que permita leer una nota entre 0.0 y 5.0. Imprimir su nota 
cualitativa equivalente. Teniendo en cuenta la siguiente tabla.
'''

nota=float(input("Ingrese su nota: "))
if nota>= 4.6 and nota<= 5.0 :
    print("Su nota es Excelente")
elif nota>= 3.6 and nota<= 4.5 :
    print("Su nota es Buena")
elif nota>= 3.0 and nota<= 3.6 :
    print("Su nota es Aceptable")
elif nota>= 2.0 and nota<= 3.0 :
    print("Su nota es Insuficiente")
elif nota<= 2.0 and nota>= 0.0 :
    print("Su nota es Deficiente")