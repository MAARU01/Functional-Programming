from hanoiRecursive import hanoi_Recursivo
from hanoiIteractive import hanoi_Iteractivo
from hanoi_mixto import hanoi_mixto 
from pila import pila
import time

def hanoi_Juego (optMetodo: int) -> str: 
    num=int (input("Ingrese el número de discos: "))
    inicio = time.time()
    origen = pila(num)
    destino =pila (num)
    auxiliar = pila (num)
    if optMetodo == 1:
        time.sleep(1)
        hanoi_Iteractivo(num,'A','B','C',origen,auxiliar,destino)
    if optMetodo == 2:
        time.sleep(1)
        hanoi_Recursivo(num,'A','B','C')
    if optMetodo == 3:
        time.sleep(1)
        hanoi_mixto(num,'A','B','C')
    print ("El tiempo de ejecución fue de: ", time.time() - inicio)

def menu () -> int:
    bienvenida  = """
    Bievenido a Torres de Hanoi,
    en este programa se muestran las 
    diferentes soluciones que existen 
    para este juego.
    1. Hanoi Iterativo
    2. Hanoi Recursivo
    3. Hanoi Iterativo-Recursivo
    """
    print (bienvenida)
    opt= int (input ("Ingrese el tipo de solución que desea ver: "))
    return opt

if __name__ == "__main__":
    tipo = menu ()
    hanoi_Juego(tipo)