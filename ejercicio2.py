'''Resolver la siguiente ecuación, teniendo en cuenta que solo se puede realizar si la 
variable r es diferente de 2; en caso contrario hacer P=1
P=(r-2)3
'''

r=float(input("Ingrese el valor de la variable: "))
if r!=2 :
    p=(r-2)**3
    print(f"El resultado de la ecuacion es: {p}")
    
else:
    print("p=1")