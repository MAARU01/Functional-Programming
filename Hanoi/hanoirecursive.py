
def hanoi_Recursivo (discos:int, torre1 : str , torre2 : str  , torre3 : str )-> str:
    if discos > 0 :
        hanoi_Recursivo (discos - 1 , torre1, torre3, torre2)
        print ("Se mueve el disco", discos , "de la torre",torre1, "a la torre", torre3)
        hanoi_Recursivo(discos-1 , torre2, torre1, torre3)