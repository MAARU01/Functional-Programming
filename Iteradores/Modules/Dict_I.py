def medals_only_dict(data_csv: list):
    country = map (lambda x: x['Country'], data_csv)
    aux = map (lambda x : {'Medals':[x['Gold Medal'], x['Silver Medal'], x['Bronze Medal']],'Total':x['Total'], 'Rank By Total':x['Rank By Total']}, data_csv)
    medallas = zip (country,aux)
    return dict(medallas)

def total_medals_above_10(data_csv: list):
    #ganadores = {i['Country']: i for i in data_csv if int(i['Total']) < 10}
    Country = map(lambda x: x['Country'], filter (lambda x: int(x['Total'])<10, data_csv))
    aux = filter (lambda x: int (x['Total'])<10, data_csv)
    ganadores = zip (Country,aux)
    return dict(ganadores)

def all_values_dict(data_csv: list):
    todos = {i['Country']: i for i in data_csv} 
    country = map (lambda x: x['Country'], data_csv)
    aux = iter(data_csv)
    todos = zip (country, aux)
    return dict (todos)

def at_least_one_gold_medal(data_csv: list):
    oros = {i['Country']: i for i in data_csv if int(i['Gold Medal']) >= 1}
    Country = map(lambda x: x['Country'], filter (lambda x: int(x['Gold Medal'])>=1, data_csv))
    aux = filter (lambda x: int (x['Gold Medal'])>=1, data_csv)
    oros = zip (Country,aux)
    return dict(oros)

def at_least_one_silver_medal(data_csv: list):
    platas = {i['Country']: i for i in data_csv if int(i['Silver Medal']) >= 1}
    Country = map(lambda x: x['Country'], filter (lambda x: int (x['Silver Medal'])>=1, data_csv))
    aux = filter (lambda x: int (x['Silver Medal'])>=1, data_csv)
    platas = zip (Country, aux)
    return dict(platas)