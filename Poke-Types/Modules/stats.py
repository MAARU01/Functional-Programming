from operator import itemgetter

def busqueda_stat (lista: list, stat: str, parametros: int) -> dict :
    if stat == 'HP':
        pokemon_stat = map (lambda x: x['Name'], filter (lambda x: int (x['HP']) == parametros, lista))
        aux = filter (lambda x: int (x['HP']) == parametros, lista)
    if stat == 'Attack':
        pokemon_stat = map (lambda x: x['Name'], filter (lambda x: int (x['Attack']) == parametros, lista))
        aux = filter (lambda x: int (x['Attack']) == parametros, lista)
    if stat == 'Defense':
        pokemon_stat = map (lambda x: x['Name'], filter (lambda x: int (x['Defense']) == parametros, lista))
        aux = filter (lambda x: int (x['Defense']) == parametros, lista)
    if stat == 'Special Attack':
        pokemon_stat = map (lambda x: x['Name'], filter (lambda x: int (x['Special Attack']) == parametros, lista))
        aux = filter (lambda x: int (x['Special Attack']) == parametros, lista)
    if stat == 'Special Defense':
        pokemon_stat = map (lambda x: x['Name'], filter (lambda x: int (x['Special Defense']) == parametros, lista))
        aux = filter (lambda x: int (x['Special Defense']) == parametros, lista)
    if stat == 'Speed':
        pokemon_stat = map (lambda x: x['Name'], filter (lambda x: int (x['Speed'] )== parametros, lista))
        aux = filter (lambda x: int (x['Speed']) == parametros, lista)
    return dict (zip (pokemon_stat,aux))

def pokemon_rompemuros (lista: list, generacion: int) -> tuple:
    rompemuro = map (lambda x: (x['Name'],int (x['HP']+x['Attack'])), filter (lambda x: int (x['Generation']) == generacion and int ((x['HP']+x['Attack']))/2 >= 3000, lista))
    return tuple(rompemuro)

def pokemon_muros (lista: list, generacion: int) -> tuple:
    muro = map (lambda x: (x['Name'],int (x['Defense']+x['Special Defense'])), filter (lambda x: int (x['Generation']) == generacion and int ((x['Defense']+x['Special Defense']))/2 >= 3000, lista))
    return tuple(muro)

def pokemon_striker (lista: list,generacion: int) -> tuple :
    striker = map (lambda x: (x['Name'],int (x['Speed']+x['Special Attack'])), filter (lambda x: int (x['Generation']) == generacion and int ((x['Speed']+x['Attack']))/2 >= 3000, lista))
    return tuple(striker)

def pokemon_poderosos (lista: list, generacion: int) -> set:
    aux = filter (lambda x: int (x['Generation']) == generacion,lista) 
    poderosos = map (lambda x: (x['Name']), filter (lambda x: int (x['Total']) >=300, aux))
    return set(poderosos) 

def pokemon_debiles (lista: list,generacion: int) -> set: 
    aux = filter (lambda x: int (x['Generation']) == generacion,lista) 
    debiles = map (lambda x: (x['Name']), filter (lambda x: int (x['Total']) <=300, aux))
    return set(debiles)

def poderosos_tipo (lista: list, tipo: str ) -> tuple:
    aux = map (lambda x: (x['Name'], x['Total']), filter (lambda x: (x["Type"] == tipo or x["Other Type"] == tipo), lista))
    poder_tipo = max ( tuple (aux) , key = itemgetter(1))
    return poder_tipo

def debiles_tipo (lista: list, tipo = str) -> tuple: 
    aux = map (lambda x: (x['Name'], x['Total']), filter (lambda x: (x["Type"] == tipo or x["Other Type"] == tipo), lista))
    debil_tipo = min ( tuple (aux) , key = itemgetter(1))
    return debil_tipo