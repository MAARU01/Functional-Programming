
class Casilla:
    es_visible:         bool
    esta_seleccionada:  bool 
    simbolo:            str

    #Constructor
    def __init__(self, simbolo_inicial: str = "", es_visible_inicial: bool = False, seleccion: bool = False) -> None:
        self.es_visible = es_visible_inicial
        self.simbolo = simbolo_inicial
        self.esta_seleccionada = seleccion
    
    
    def set_simbolo(self,simbolo:str) -> None:
        self.simbolo = simbolo

    def get_simbolo(self) -> str:
        return self.simbolo

    def set_esta_seleccionada(self,estado: bool) -> None:
        self.esta_seleccionada = estado

    def get_esta_seleccionada(self) -> bool:
        return self.esta_seleccionada

    def cambiar_visibilidad(self) -> None:
        self.es_visible = True if self.es_visible == False else False

    def get_es_visible(self) -> bool:
        return self.es_visible