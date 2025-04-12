#Desafio 19

#Crie um loop que peça ao usuário para digiar o nome de uma fruta. Se a fruta digitada não for 'abacate', o loop deve continuar pedindo ao usuário para digitar o nome de uma fruta. Se a fruta for 'abacate', o loop deve terminar e o programa deve imprimir 'Parabéns, você acertou a fruta!'.


while True:
    fruta = input('Tente descobrir qual fruta está no código. Escreva aqui uma: ')
    if fruta.lower() == 'abacate':
        break
print('Parabéns, você acertou a fruta!')