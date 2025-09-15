import sys 
from pila import pila

def movimiento_Discos (origen : pila, destino: pila, torre_origen : str, torre_destino : str) -> str:
    TopDiscoTorre1 = pila.Pop(origen)
    TopDiscoTorre2 = pila.Pop(destino)

    if (TopDiscoTorre1 == -sys.maxsize):
        pila.push(origen, TopDiscoTorre2)
        print ("Se mueve el disco", TopDiscoTorre2 , "de la torre",torre_destino, "a la torre", torre_origen)
       
    elif (TopDiscoTorre2 == -sys.maxsize):
        pila.push(destino, TopDiscoTorre1)
        print ("Se mueve el disco", TopDiscoTorre1 , "de la torre",torre_origen, "a la torre", torre_destino)
       
    elif (TopDiscoTorre1 > TopDiscoTorre2):
        pila.push(origen, TopDiscoTorre1)
        pila.push(origen, TopDiscoTorre2)
        print ("Se mueve el disco", TopDiscoTorre2 , "de la torre",torre_destino, "a la torre", torre_origen)
       
    else:
        pila.push(destino, TopDiscoTorre2)
        pila.push(destino, TopDiscoTorre1)
        print ("Se mueve el disco", TopDiscoTorre1 , "de la torre",torre_origen, "a la torre", torre_destino)

def hanoi_Iteractivo (discos : int , torre1 : str, torre2 : str, torre3 : str, pila1 : pila, pila2: pila, pila3: pila) -> None:
    if (discos % 2 == 0):
        temp = torre3
        torre3 = torre2 
        torre2 = temp
    total_de_movimientos = int(pow(2, discos) - 1)

    for i in range(discos, 0, -1):
        pila.push(pila1, i)
   
    for i in range(1, total_de_movimientos + 1):
        if (i % 3 == 1):
             movimiento_Discos(pila1, pila2, torre1, torre3)
        elif (i % 3 == 2):
             movimiento_Discos(pila1, pila3, torre1, torre2)
        elif (i % 3 == 0):
             movimiento_Discos(pila3, pila2, torre2, torre3)