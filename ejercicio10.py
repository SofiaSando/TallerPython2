'''Elabore un algoritmo que lea el nombre, la edad, el sexo (F: Femenino, M: 
masculino) y el estado civil(1:Casado,2:soltero,3:Separado,4: otro) de una persona 
que desea participar en las elecciones este año. Si es menor de edad imprimir 
mensaje que diga que no puede votar, de lo contrario imprimir el mensaje 
indicado la mesa en la cual le corresponde votar.'''

nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese la edad: "))
sexo=input("Ingrese el texto (F:Femenino, M:Masculino): ")
sexo1=sexo.upper()
estadoCivil=int(input("Ingreseel estado civil (1:Casado,2:soltero,3:Separado,4: otro): "))
if edad<18 :
    print("No puede votar porque es menor de edad")
elif sexo1=="F" and estadoCivil==1 :
    print(f"Señor/a {nombre} Vota en la mesa 1")
elif sexo1=="F" and estadoCivil==2 :
    print(f"Señor/a {nombre} Vota en la mesa 2")
elif sexo1=="F" and estadoCivil==3 :
    print(f"Señor/a {nombre} Vota en la mesa 3")
elif sexo1=="F" and estadoCivil==4 :
    print(f"Señor/a {nombre} Vota en la mesa 4")
elif sexo1=="M" and estadoCivil==1 :
    print(f"Señor/a {nombre} Vota en la mesa 5")
elif sexo1=="M" and estadoCivil==2 :
    print(f"Señor/a {nombre} Vota en la mesa 6")
elif sexo1=="M" and estadoCivil==3 :
    print(f"Señor/a {nombre} Vota en la mesa 7")
elif sexo1=="M" and estadoCivil==4 :
    print(f"Señor/a {nombre} Vota en la mesa 8")
