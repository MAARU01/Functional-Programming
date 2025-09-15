import csv
import pprint 
pp = pprint.PrettyPrinter(indent=4)
print_nice = lambda object_print : pp.pprint(object_print)
def leer_csv_generador(archivo: str):
    with open(archivo) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country = {key: value for key, value in iterable}
            data.append(country)
    return (iterador for iterador in data)