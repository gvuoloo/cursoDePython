#Desafio 21

#Para este desafio, crie uma lista com os nomes de três cidades. Peça ao usuário para digitar o nome de uma cidade. Se a cidade estiver na lista, imprima "A cidade está na lista de cidades". Se a cidade não estiver na tupla, imprima: "A cidade não está na lista de cidades".

cidades = ('Cuiabá', 'Rio de Janeiro', 'Hangzhou', 'Lisboa', 'Campinas', 'São Paulo')

cidade_user = input('Insira uma cidade: ')
if cidade_user in cidades:
    print(f'{cidade_user} está na lista de cidades.')
else:
    print(f'{cidade_user} não está na lista de cidades.')