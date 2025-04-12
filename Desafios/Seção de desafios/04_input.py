#Desafio 04

#Neste desafio, quero que você crie um script que pergunte o nome e a idade do usuário usando a função input(). Depois disso, o script deve imprimri uma mensagem que diga "Olá, [nome]! Você tem [idade] anos."

name = input(str(f'Por favor, insira o seu nome: '))
age = int(input(f'Por favor, insira quantos anos você tem: '))

print(f'Olá, {name}! Você tem {age} anos!')