lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
vogais = ['A', 'E', 'I', 'O', 'U']

# Seu código aqui

for nome in lista_nomes:
	for vogal in vogais:
		first = nome[0]
		if first == vogal:
			print(nome)
		if first == vogal.lower():
			print(nome)