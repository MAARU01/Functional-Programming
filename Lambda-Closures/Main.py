import pprint
from Modules import List_I as l_comp
from Modules import Set_I as s_comp
from Modules import Dict_I as d_comp
from Modules import Set_O as s_op
import csv
import os

def read_csv() -> list:
    with open("./assets/tokyo_medals_2021.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []

        for row in reader:

            iterable = zip(header, row)

            country = {key: value for key, value in iterable}
            data.append(country)
    return data


if __name__ == "__main__":
    # Variables necesarias
    pp = pprint.PrettyPrinter(indent=4)
    print_nice = lambda object_print : pp.pprint(object_print)
    data_csv = read_csv()
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"


    # print("""
    #     Opciones de tarea:
    # 1. Comprehensions de listas
    # 2. Comprehensions de diccionarios
    # 3. Comprehensions de Sets
    # 4. Operación de conjuntos
    # 5. Salir del programa
    # """)
    opcion : int = 0
    # opcion = int(input("Seleccione una opción del menu: "))
    opciones_internas : int = 0
    
    while opcion != 5:
        
        print("""
        Opciones de tarea:
    1. Comprehensions de listas
    2. Comprehensions de diccionarios
    3. Comprehensions de Sets
    4. Operación de conjuntos
    5. Salir del programa
    """)
        opcion = 0
        opcion = int(input("Seleccione una opción del menu: "))
        opciones_internas = 0
        os.system(var)
        if opcion == 1:
            # List comprehension parte del menu
            print("""
            List Comprehensions:
        1. Crear una lista de diccionarios con todos los registros y datos del csv
        2. Crear una lista de tuplas con todos los registros y columnas `Country` y `Rank By Total`
        3. Crear una lista de tuplas que contenga `Country` y `Total` donde el total de medallas sea > 40
        4. Crear una lista de tuplas que contenga `Country` y `Total` donde el total de medallas sea <= 20
        5. Crear una lista de diccionarios de todos los registros hayan ganado las 3 medallas 
            """)  
            opciones_internas = int(input("Seleccione una opción del menu: "))
            os.system(var)
            if opciones_internas == 1:
                print_nice(l_comp.all_values_dict(data_csv))
            elif opciones_internas == 2:
                print_nice(l_comp.tuples_countries(data_csv))
            elif opciones_internas == 3:
                print_nice(l_comp.total_medals_over_40(data_csv))
            elif opciones_internas == 4:
                print_nice(l_comp.total_medals_above_20(data_csv))
            elif opciones_internas == 5:
                print_nice(l_comp.each_medal_teams(data_csv))
            else:
                print("Opción incorrecta")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)
        elif opcion == 2:
            #Dict comprehension parte del menu
            print("""
            Dict comprehensions:

            Donde la clave de cada diccionario sea el nombre del país:
        1. Crear un diccionario con diccionarios todos los registros del csv excepto que los registro `Gold Medal`,`Silver Medal`,`Bronce Medal` estaran en un atributo (Lista) del diccionario llamado `Medals` 
        2. Crear un diccionario de diccionarios con todos los registros del csv donde el total de medallas sea < 10
        3. Crear un diccionario de diccionarios con todos los registros y datos del csv
        4. Crear un diccionario de diccionarios con todos los registros donde contenga minimo una medalla de oro
        5. Crear un diccionario de diccionarios con todos los registros donde tenga minimo una medalla de plata
            """)

            opciones_internas = int(input("Seleccione una opción del menu: "))
            os.system(var)
            if opciones_internas == 1:
                print_nice(d_comp.medals_only_dict(data_csv))
            elif opciones_internas == 2:
                print_nice(d_comp.total_medals_above_10(data_csv))
            elif opciones_internas == 3:
                print_nice(d_comp.all_values_dict(data_csv))
            elif opciones_internas == 4:
                print_nice(d_comp.at_least_one_gold_medal(data_csv))
            elif opciones_internas == 5:
                print_nice(d_comp.at_least_one_silver_medal(data_csv))
            else:
                print("Opción incorrecta")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)
            
        elif opcion == 3:
            #Set comprehension
            print("""
            Set Comprehensions
        1. Crear un conjunto de todos los registros donde sus elementos esten formados por una tupla (`Country`) donde tenga minimo una medalla de oro
        2. Crear un conjunto de todos los registros donde sus elementos esten formados por una tupla (`Country`) donde tenga minimo una medalla de plata
        3. Crear un conjunto de todos los registros donde sus elementos esten formados por una tupla (`Country`) donde tenga minimo una medalla de bronce
        4. Crear un conjunto de todos los registros donde sus elementos esten formados por una tupla (`Country`,`Total`) 
        5. Crear un conjunto de todos los registros donde sus elementos esten formados por una tupla (`Country`,`Rank Total`) 
            """)

            opciones_internas = int(input("Seleccione una opción del menu: "))
            os.system(var)
            if opciones_internas == 1:
                print_nice(s_comp.country_gold_medals(data_csv))
            elif opciones_internas == 2:
                print_nice(s_comp.country_silver_medals(data_csv))
            elif opciones_internas == 3:
                print_nice(s_comp.country_bronce_medals(data_csv))
            elif opciones_internas == 4:
                print_nice(s_comp.all_values_set(data_csv))
            elif opciones_internas == 5:
                print_nice(s_comp.country_all_medals(data_csv))
            else:
                print("Opción incorrecta")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)
        elif opcion == 4:
            #Set comprehension
            print("""
            Operaciones de Conjuntos
        1. Mediante operacion de conjuntos obtener que paises tienen de los 3 tipos de medallas 
        2. Mediante operacion de conjuntos obtener que paises no tienen medallas de oro pero si tienen de plata y bronce
        3. Mediante operacion de conjuntos obtener que paises no tienen medallas de oro ni de plata pero si de bronce
        4. Mediante operacion de conjuntos obtener que paises se encuentran en el ejercicio 3 de set comprehensions pero no en el conjunto 2
        5. Mediante operacion de conjuntos obtener que paises se encuentran en el ejercicio 2 de set comprehensions pero no en el conjunto 3
            """)

            opciones_internas = int(input("Seleccione una opción del menu: "))
            os.system(var)
            if opciones_internas == 1:
                clousure = s_op.countries_with_all_medals(s_comp.country_gold_medals(data_csv))
                print_nice(clousure(s_comp.country_silver_medals(data_csv),s_comp.country_bronce_medals(data_csv)))

            elif opciones_internas == 2:
                cl_2 = s_op.countries_without_gold_medals_but_silver_and_bronce(s_comp.country_silver_medals(data_csv),s_comp.country_bronce_medals(data_csv))
                print_nice(cl_2(s_comp.country_gold_medals(data_csv)))

            elif opciones_internas == 3:
                clousure = s_op.countries_without_gold_and_silver_but_bronce(s_comp.country_bronce_medals(data_csv))
                print_nice(clousure(s_comp.country_silver_medals(data_csv),s_comp.country_gold_medals(data_csv)))

            elif opciones_internas == 4:
                clousure = s_op.exclusion_ex_2_between_3_sets(s_comp.country_silver_medals(data_csv))        
                print_nice(clousure(s_comp.country_bronce_medals(data_csv)))    
            elif opciones_internas == 5:
                clousure = s_op.exclusion_ex_3_between_2_sets(s_comp.country_bronce_medals(data_csv))
                print_nice(clousure(s_comp.country_silver_medals(data_csv)))
            else:
                print("Opción incorrecta")
            aux_char = input('Presione cualquier tecla para continuar').split(" ")[0]
            os.system(var)
        else:
            print("Saliendo del programa")