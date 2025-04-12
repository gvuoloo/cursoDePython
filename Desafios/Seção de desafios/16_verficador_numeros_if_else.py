#Desafio 16

#Para este desafio, quero que você peça ao usuário que digite um número. Se o número for maior que 10, imprima "O número é maior que 10". Caso contrário, imprima "O número é menor ou igual a 10".

num = float(input('Por favor, insira um número:'))
if num > 10:
    print(f'O número {num} é maior que 10.')
else:
    print(f'O número {num} é menor ou igual a 10.')