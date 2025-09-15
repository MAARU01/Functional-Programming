def countries_with_all_medals(gold_medals_countries: set):
    def intersection_medals(silver_medals_countries: set, bronce_medals_countries: set):
        return gold_medals_countries.intersection(silver_medals_countries,bronce_medals_countries)
    return intersection_medals

def countries_without_gold_medals_but_silver_and_bronce(silver_medals_countries: set, bronce_medals_countries:set):
    set_without_gold_medals = silver_medals_countries.intersection(bronce_medals_countries)
    def filter_medals(gold_medals_countries: set) -> set:
        return set_without_gold_medals.difference(gold_medals_countries)
    return filter_medals

def countries_without_gold_and_silver_but_bronce(bronce_medals_countries: set):
    def intersection_bronce(silver_medals_countries: set, gold_medals_countries: set) -> set:
        return bronce_medals_countries.difference(silver_medals_countries,gold_medals_countries)
    return intersection_bronce

def exclusion_ex_2_between_3_sets(set_exercise_2: set):
    def operation_sets(set_exercise_3: set) -> set:
        return set_exercise_3.difference(set_exercise_2)
    return operation_sets

def exclusion_ex_3_between_2_sets(set_exercise_3: set):
    def operation_sets(set_exercise_2: set) -> set:
        return set_exercise_2.difference(set_exercise_3)
    return operation_sets