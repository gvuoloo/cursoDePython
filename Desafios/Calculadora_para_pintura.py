# Desafio com funções
'''

Criar um programa que calcule a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguientes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem "Você necessita de X latas de tintas."

'''
print('Para comprar a quantidade correta de tinta para se pintar uma parede, você deverá fornecer dados como rendimento (em m²) da tinta e a área (em m²) da superfície que será pintada.')

rendimento = (float(input('Insira o rendimento da tinta, em m²: ')))

larg = float(input('Insira a largura, em metros, da superfície a ser pintada: '))

alt = float(input('Insira a altura, em metros, da superfície a ser pintada: '))


def calculo_tinta():    
    area = larg * alt
    lata = area/rendimento
    lata = int(lata) + 1 if lata > int(lata) else int(lata)
    print(f'A quantidade de latas de tintas necessárias para se pintar a parede será de, pelo menos {lata}.')

calculo_tinta()