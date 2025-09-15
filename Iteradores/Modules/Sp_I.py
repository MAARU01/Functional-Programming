def countries_with_all_medals(conjunto_1: set, conjunto_2: set, conjunto_3:set):
    return conjunto_1.intersection(conjunto_2,conjunto_3)

def countries_without_gold_medals_but_silver_and_bronce(conjunto_1: set, conjunto_2: set, conjunto_3: set):
    return conjunto_1.intersection(conjunto_2).difference_update(conjunto_3)

def countries_without_gold_and_silver_but_bronce(conjunto_1: set, conjunto_2: set, conjunto_3: set):
    return conjunto_1.difference(conjunto_2,conjunto_3)

def exclusion_ex_2_between_3_sets(conjunto_1: set, conjunto_2: set):
    return conjunto_1.difference(conjunto_2)