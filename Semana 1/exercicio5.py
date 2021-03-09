lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

# Seu código aqui

for frase in lista_frases:
	palavras = frase.split(' ')
	for palavra in palavras:
		gerundio = palavra[-4:]
		if gerundio == 'ando':
			print(palavra)
		if gerundio == 'endo':
			print(palavra)
		if gerundio == 'indo':
			print(palavra)