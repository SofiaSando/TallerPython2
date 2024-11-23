'''Una persona no tiene claridad sobre el dispositivo que desea comprar para su 
portátil . La decisión la tomará de acuerdo con una bonificación que recibirá de 
parte de la empresa donde labora. Si recibe menos de $50.000 comprará una 
cámara web. Si recibe entre $50.000 y $200.000 comprará un subwoofer. Si recibe 
más de $200.000 y hasta $500.000 se comprará un DD externo. Si recibe más de 
$500.000 y hasta $1.000.000 se compra una impresora multifuncional. Y si recibe 
más de un $1.000.000 se comprará un proyector.
Realice un algoritmo para ayudarle a esta persona a comprar un dispositivo.
'''

bonificacion=float(input("Ingrese el valor de su bonificacion: "))
if bonificacion<50000 :
    print(f"Compre una camara web ya que su bonificacion es de: {bonificacion}")
elif bonificacion>=50000 and bonificacion<=200000 :
    print(f"Compre un subwoofer ya que su bonificacion es de: {bonificacion}")
elif bonificacion>200000 and bonificacion<=500000 :
    print(f"Compre un DD externo ya que su bonificacion es de: {bonificacion}")
elif bonificacion>500000 and bonificacion<=1000000 :
    print(f"Compre una impresora multifuncional ya que su bonificacion es de: {bonificacion}")
elif bonificacion>1000000 :
    print(f"Compre un proyector ya que su bonificacion es de: {bonificacion}")


