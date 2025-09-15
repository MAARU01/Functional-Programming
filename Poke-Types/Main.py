import os
from Modules import lectura_archivo import *
from Modules import funciones import *
from Modules import menu import *
from Modules import stats import *
if __name__ == '__main__':
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    opcion : int = 0
    opciones_internas : int = 0
    while opcion != 3:
        datos = leer_csv_generador ("./Assets/pokemon-data.csv")
        menu_general()
        opcion = 0
        opcion = int(input("Seleccione una opción del menu: "))
        opciones_internas = 0
        os.system(var)
        sub = submenu()
        if opcion == 1 :
            sub (1)
            opciones_internas = int(input("Seleccione una opción del menu: "))
            os.system(var)
            if opciones_internas == 1:
                nombre = input ("Ingresa el nombre del Pokemon: ")
                print_nice(filtrar_pokemon_lista(datos,'Name',nombre))
            elif opciones_internas == 2: 
                gen = input ("Ingresa la generación: ")
                print_nice(filtrar_pokemon_lista(datos,'Generation',gen))
            elif opciones_internas == 3:
                print_nice (filtrar_pokemon_tupla(datos,'Legendary','1'))
            elif opciones_internas == 4:
                print_nice(obtener_tipos(datos))
            elif opciones_internas == 5:
                tip = input ("Ingresa el tipo elemental: ")
                print_nice(filtrar_pokemon_tipo(datos,tip))
            elif opciones_internas == 6: 
                imprimir_iniciales(datos)
            else: 
                print ("Opción incorrecta")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)
        elif opcion == 2 :
            sub (2)
            opciones_internas = int(input("Seleccione una opción del menu: "))
            os.system(var)
            if opciones_internas == 1:
                stat = input ("Ingrese el stat a buscar: ")
                param = int (input("Ingrese el número de puntos del stat: "))
                print_nice (busqueda_stat(datos,stat,param))
            elif opciones_internas == 2: 
                gen = input ("Ingrese la generación del Pokémon: ")
                print_nice (pokemon_rompemuros(datos,int(gen)))
            elif opciones_internas == 3:
                gen = input ("Ingrese la generación del Pokémon: ")
                print_nice (pokemon_muros(datos,int(gen)))
            elif opciones_internas == 4:
                gen = input ("Ingrese la generación del Pokémon: ")
                print_nice (pokemon_striker(datos,int(gen)))
            elif opciones_internas == 5:
                gen = input ("Ingrese la generación del Pokémon: ")
                print_nice (pokemon_poderosos(datos,int(gen)))
            elif opciones_internas == 6: 
                gen = input ("Ingrese la generación del Pokémon: ")
                print_nice (pokemon_debiles(datos,int(gen)))
            elif opciones_internas == 7:
                tip = input ("Ingrese el tipo elemental a buscar: ")
                print_nice (poderosos_tipo(datos,tip))
            elif opciones_internas == 8:
                tip = input ("Ingrese el tipo elemental a buscar: ")
                print_nice (debiles_tipo(datos,tip))
            else: 
                print ("Opción incorrecta")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)
        elif opcion == 3 :  
            print("Saliendo del programa")
        else: 
            print ("¡A ver por ahí! Esa opción es inexistente")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)