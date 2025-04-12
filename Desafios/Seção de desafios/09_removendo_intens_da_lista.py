#Desafio 09

#Para este desafio, quero que você use a lista 'frutas' do desafio 06. 
#Primeiro, remova 'manga' da lista usando o método remove().
#Segundo, remova o último item da lista utilizando o comando del. 
#Por fim, imprima a lista modificada em tela.

frutas = ['maçã', 'banana', 'manga', 'uva']

frutas.remove('manga')
del frutas[-1]

print(frutas)