import csv
from datetime import date
import datetime

def find_born_monday(lista):
    lista_final = []
    for registro in lista:
        if registro[4] != 'birthdate':
            try:
                birthdate = datetime.datetime.strptime(registro[4], '%Y-%m-%d')
                if birthdate.weekday() == 0:
                    lista_final.append(registro[0])
            except:
                pass
    return lista_final


def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.
    Args:
        path (String): Nome do arquivo
    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    nascidos_segunda_feira = find_born_monday(lista)
    for item in nascidos_segunda_feira:
        print(item)