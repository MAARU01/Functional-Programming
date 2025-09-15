import typing_extensions


def medals_only_dict(data_csv: list) -> dict[str,dict]:
    medallas = {i['Country']:{'Medals':[i['Gold Medal'], i['Silver Medal'], i['Bronze Medal']],'Total':i['Total'], 'Rank By Total':i['Rank By Total']} for i in data_csv}
    return medallas

def total_medals_above_10(data_csv: list) -> dict[str,dict]:
    ganadores = {i['Country']: i for i in data_csv if int(i['Total']) < 10}
    return ganadores

def all_values_dict(data_csv: list) -> dict[typing_extensions.Any,dict]:
    todos = {i['Country']: i for i in data_csv}
    return todos

def at_least_one_gold_medal(data_csv: list) -> dict[str,dict]:
    oros = {i['Country']: i for i in data_csv if int(i['Gold Medal']) >= 1}
    return oros

def at_least_one_silver_medal(data_csv: list) -> dict[str,dict]:
    platas = {i['Country']: i for i in data_csv if int(i['Silver Medal']) >= 1}
    return platas