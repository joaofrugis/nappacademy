lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']
lista_nomes = lista_nomes + ['Mário', 'Arnaldo', 'Lucas', 'Maria Vitória']
lista_nomes = lista_nomes + ['Vitor', 'Ana Paula', 'Maria Aparecida']

# Seu código aqui

for nome in lista_nomes:
	if ' ' in nome:
		print(nome)