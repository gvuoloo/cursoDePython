#Desafio 22

#Para este desafio, crie uma lista com 5 nomes de países e as capitais desses países. Peça ao usuário para digitar o nome de um país. Se o país estiver na lista, imprima "A capital do país [país] é [capital]". Se o país não estiver na lista, "Desculpe-nos, não temos informações sobre a capital desse país."

#1 criar um DICIONÁRIO:

paises_capitais = {
    'Brasil' : 'Brasília',
    'China' : 'Pequim',
    'Argentina': 'Buenos Aires',
    'Portugal' : 'Lisboa',
    'Rússia' : 'Moscou'
}

#2 pedir ao usuário para inserir um país:

pais_user = input(f'Insira aqui o nome de um país para ter a informação de qual é a sua capital:')

#3 Verificar o país do usuário:

if pais_user in paises_capitais:
    print(f'A capital do país {pais_user} é: {paises_capitais[pais_user]}.')
else:
    print('Desculpe-nos, não temos informações sobre a capital desse país.')