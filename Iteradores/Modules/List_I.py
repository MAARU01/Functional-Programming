def all_values_dict(data_csv: list):
    all_values = iter(data_csv)
    return all_values

def tuples_countries(data_csv: list):
    list_tuples_country = map (lambda x: (x["Country"],x['Rank By Total']), filter (lambda x: int(x["Total"]) <= 20, data_csv))
    return list_tuples_country

def total_medals_over_40(data_csv: list):
    list_tuples_medals_major = map (lambda x: (x["Country"], x["Total"]), filter (lambda x: int(x["Total"]) > 40, data_csv))
    return list_tuples_medals_major

def total_medals_above_20(data_csv: list):
    list_tuples_medals_minor = map (lambda x: (x["Country"], x["Total"]), filter (lambda x: int(x["Total"]) <= 20, data_csv))
    return  list_tuples_medals_minor

def each_medal_teams(data_csv: list):
    list_dict_all_type_medals = filter (lambda x: int(x["Bronze Medal"]) >= 1 and int(x["Silver Medal"]) >= 1 and int(x["Gold Medal"]) >= 1, data_csv)
    return list_dict_all_type_medals