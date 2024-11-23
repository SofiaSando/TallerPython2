''' En las pruebas de ICFES, se presentan dos tipos de prueba: Una de aptitud 
matemática y otra de lenguaje. Leer los puntajes obtenidos por un estudiante en 
cada prueba e imprimir en cual obtuvo mayor puntaje. Tenga en cuenta que 
ambos puntajes podrían ser iguales.
'''

puntajeMatematicas=float(input("Ingrese el puntaje de la prueba de aptitud matematica: "))
puntajeLenguaje=float(input("Ingrese el puntaje de la prueba de lenguaje: "))
if puntajeMatematicas>puntajeLenguaje :
    print(f"Tuvo mayor puntaje en la prueba de aptitud matematica, su puntaje es: {puntajeMatematicas} ")
elif puntajeLenguaje>puntajeMatematicas :
    print(f"Tuvo mayor puntaje en la prueba de lenguaje, su puntaje es: {puntajeLenguaje} ")
elif puntajeLenguaje==puntajeMatematicas :
    print(f"Tuvo el mismo puntaje en ambas pruebas, su puntaje es {puntajeMatematicas} y {puntajeLenguaje}")
