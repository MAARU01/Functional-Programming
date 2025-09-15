def all_values_dict(data_csv: list) -> list[dict]:
    all_values = [element for element in data_csv]
    return all_values

def tuples_countries(data_csv: list) -> list[tuple[str,str]]:
    list_tuples_country = [(element['Country'], element['Rank By Total']) for element in data_csv]
    return list_tuples_country

def total_medals_over_40(data_csv: list) -> list[tuple[str,str]]:
    list_tuples_medals_major = [(element["Country"], element["Total"]) for element in data_csv if int(element["Total"]) > 40]
    return list_tuples_medals_major

def total_medals_above_20(data_csv: list) -> list[tuple[str,str]]:
    list_tuples_medals_minor = [(element["Country"], element["Total"]) for element in data_csv if int(element["Total"]) <= 20]
    return list_tuples_medals_minor

def each_medal_teams(data_csv: list) -> list[dict]:
    list_dict_all_type_medals = [element for element in data_csv if int(element["Bronze Medal"]) >= 1 and int(element["Silver Medal"]) >= 1 and int(element["Gold Medal"]) >= 1]
    return list_dict_all_type_medals