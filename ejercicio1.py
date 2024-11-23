'''Hacer un programa para un laboratorio de Química, que lea un símbolo químico e 
imprimir a que elemento al cual corresponde. Nota. Tenga presente que solo se cuenta con los elementos de Hidrogeno, 
oxígeno y nitrógeno. En los demás casos se debe imprimir un mensaje: 
“Elemento no encontrado”
'''

simbolo=input("Digite el simbolo en mayuscula: ")
simbolo1=simbolo.upper()
if simbolo1=="H" :
    print("El elemento es Hidrogeno")
if simbolo1=="O" :
    print("El elemento es Oxigeno")
if simbolo1=="N" :
    print("El elemento es Nitrogeno")
else:
    print("Elemento NO encontrado")