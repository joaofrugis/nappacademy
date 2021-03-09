from massa_dados import list_spend_money


def spend_by_login(login, limit=1000):
	for register in list_spend_money:
		name, user, sex, spend = register
		if user == login:
			try:
				if register[3] < limit:
					print(register)
			except:
				pass 
		


def sum_by_login(login, limit=1000):
	soma = 0
	for register in list_spend_money:
		name, user, sex, spend = register
		if user == login:
			try:
				if register[3] < limit:
					soma += register[3]
			except:
				pass

	return soma


if __name__ == "__main__":
	login = 'justin16'
	spend_by_login(login, 1200)
	print('A soma total até 600: ')
	print(sum_by_login(login))
	print('A soma total até 1200: ')
	print(sum_by_login(login, 1200))