import sys 
class pila:
     def __init__(self,tamanio: int) -> None:
         self.tamanio = tamanio
         self.tope = -1
         self.items = []
    
     def isFull(self) -> int:
        return (self.tope == (self.tamanio - 1))
    
     def isEmpty(self) -> int:
        return (self.tope == -1)
    
     def push(self, item: int) -> None:
        if(self.isFull()):
            return
        self.tope+=1
        self.items.append(item)
    
     def Pop(self) -> int:
        if(self.isEmpty()):
            return -sys.maxsize
        self.tope-=1
        return self.items.pop()