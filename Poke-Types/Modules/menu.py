def menu_general () -> None:
    bienvenida = """
    Pokédex Generaciones Funcionales 
    Opciones: 
    1. General
    2. Stats
    3. Salir 
    """
    print (bienvenida)
def submenu():
    sub1 = """
    1.1 Pokemon 
    1.2 Regional  
    1.3 Legendarios 
    1.4 Tipos 
    1.5 Pokemon por Tipo
    1.6 Iniciales
    """
    sub2 = """
    2.1 Búsqueda por Stat
    2.2 Rompemuros  
    2.3 Muros
    2.4 Striker 
    2.5 Poderosos de todos los tiempos
    2.6 Débiles de todos los tiempos
    2.7 Poderoso por tipo 
    2.8 Débil por tipo 
    """
    def despliegue(op: int) -> None:
        if op == 1: 
            print (sub1)
        if op == 2: 
            print (sub2)
    return despliegue 