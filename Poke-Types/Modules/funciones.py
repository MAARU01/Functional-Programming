from lectura_archivo import print_nice
def obtener_tipos(lista:list)->set:
    tipos =set()
    tipos = {i['Type'] for i in lista}
    return tipos

def filtrar_pokemon_tipo(lista_original:list,tipo:str)->list:
    lista = [i for i in lista_original if i["Type"] == tipo or i["Other Type"] == tipo]
    return lista

def filtrar_pokemon_lista(lista_original:dict,parametro:str,valor_parametro:str)->list:
    if parametro=="Type" or parametro =="Other Type":
        lista = [i for i in lista_original if i["Type"] == valor_parametro or i["Other Type"] == valor_parametro]
    else:
        lista = [i for i in lista_original if i[parametro]==valor_parametro]
    return lista
def filtrar_pokemon_tupla(lista_original:list,parametro:str,valor_parametro:str)->tuple:
    if parametro=="Type" or parametro =="Other Type":
        tupla = (i for i in lista_original if i["Type"] == valor_parametro or i["Other Type"] == valor_parametro)
    else:
        tupla = (i for i in lista_original if i[parametro]==valor_parametro)
    return tuple(tupla)
def imprimir_pokemon_por_tipo(tipos: set, datos:list)->None: 
    for i in tipos:
        print(filtrar_pokemon_lista(datos,"Type",i))
        
def imprimir_iniciales(datos:list)->None:
    for i in range(1,9):
        generacion = filtrar_pokemon_tupla(datos,"Generation",str(i))
        print_nice(generacion[:9])