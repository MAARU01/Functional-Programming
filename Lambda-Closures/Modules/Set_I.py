def country_gold_medals(data_csv: list) -> set[tuple[str,...]]:
    gold_medals = {(i['Country']) for i in data_csv if int(i['Gold Medal'])>0}
    return gold_medals

def country_silver_medals(data_csv: list) -> set[tuple]:
    silver = {(i['Country']) for i in data_csv if int(i['Silver Medal'])>0}
    return silver

def country_bronce_medals(data_csv: list) -> set[tuple]:
    bronce = {(i['Country']) for i in data_csv if int(i['Bronze Medal'])>0}
    return bronce

def all_values_set(data_csv: list) -> set[tuple[str,str]]: 
    total = {(i['Country'],i['Total']) for i in data_csv}
    return total

def country_all_medals(data_csv: list) -> set[tuple[str,str]]:
    triple = {(i['Country'],'Triple ganador') for i in data_csv if int(i['Bronze Medal'])>0 and int(i['Gold Medal'])>0 and int(i['Silver Medal'])>0}
    return triple