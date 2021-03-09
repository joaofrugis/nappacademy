from massa_dados import list_spend_money


def spend_by_gender(gender):
    for register in list_spend_money:
    	name, user, sex, spend = register
    	if sex == gender:
    		print(register)


def sum_by_gender(gender):
    soma = 0
    for register in list_spend_money:
    	name, user, sex, spend = register
    	if sex == gender:
    		try:
    			soma += float(register[3])
    		except:
    			pass
    			
    return soma


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))