from massa_dados import list_spend_money


def spend_by_login(login):
	for register in list_spend_money:
		name, user, sex, spend = register
		if user == login:
			print(register)

def sum_by_login(login):
    soma = 0
    for register in list_spend_money:
    	name, user, sex, spend = register
    	if login == user:
    		try:
    			soma += float(register[3])
    		except:
    			pass
    	
    return soma


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))