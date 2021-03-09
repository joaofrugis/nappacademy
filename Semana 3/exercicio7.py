import csv
import json


def carregar_dicionario_websites(path):
    
    lista_names = []

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] != 'name':
                dicionario = dict()
                dicionario[row[0]] = eval(row[4])
                lista_names.append(dicionario)
    
    return lista_names
    
if __name__ == "__main__":
    path = './names.csv'
    dicionario = {}
    dicionario = carregar_dicionario_websites(path)
    json_object = json.dumps(dicionario, indent=4)
    print(json_object)