import csv


def find_born_in_month_and_gender(lista, paramether='03', gender='F'):
    lista_final = []
    for registro in lista:
        try:
            mes = registro[4].split('-')


            if paramether == mes[1] and gender == registro[5]:
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
    print(find_born_in_month_and_gender(lista))
    print(find_born_in_month_and_gender(lista, '01'))
    print(find_born_in_month_and_gender(lista, '01', 'M'))