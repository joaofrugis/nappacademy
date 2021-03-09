from massa_dados import list_spend_money


def spend_by_subname(name):
    for register in list_spend_money:
    	nome, user, sex, spend = register
    	if name in nome:
    		print(register)


def sum_by_subname(name):
    soma = 0
    for register in list_spend_money:
    	nome, user, sex, spend = register
    	if name in nome:
    		try:
    			soma += register[3]
    		except:
    			pass

    return soma

if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))