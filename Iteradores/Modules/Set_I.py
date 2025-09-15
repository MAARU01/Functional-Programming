def country_gold_medals(data_csv: list):
    gold_medals = map(lambda x: x['Country'], filter(lambda x: int(x['Gold Medal'])>0, data_csv))
    return gold_medals

def country_silver_medals(data_csv: list):
    silver = map (lambda x: x['Country'], filter(lambda x: int(x['Silver Medal'])>0, data_csv))
    return silver

def country_bronce_medals(data_csv: list):
    bronce = map (lambda x: x['Country'], filter(lambda x: int(x['Bronze Medal'])>0, data_csv))
    return bronce

def all_values_set(data_csv: list): 
    total = map (lambda x: (x['Country'],x['Total']), data_csv)
    return total

def country_all_medals(data_csv: list):
    triple = map (lambda x: (x['Country'],'Triple ganador'), filter(lambda x: int(x['Bronze Medal'])>0 and int(x['Gold Medal'])>0 and int(x['Silver Medal'])>0 , data_csv))
    return triple