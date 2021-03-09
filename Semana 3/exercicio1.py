import csv


def find_subtring_credit_card(lista, parametro='322'):
    lista_final = []
    for registro in lista:
        if parametro in registro[2]:
            lista_final.append(registro[0])

    return(lista_final)


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
    print(find_subtring_credit_card(lista))
    print(find_subtring_credit_card(lista, '222'))