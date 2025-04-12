#Desafio 05

#Neste desafio quero que você crie um script que solicite ao usuário dois números. Em seguida, seu script deve imprimri a soma, subtração, multiplicação, divisão (resultado decimal) e a exponenciação (primeiro número elevado ao segundo número) desses dois número.

num1 = int(input(f'Por favor, insira um número: '))
num2 = int(input(f'Por favor, insira um novo número: '))

soma = int(num1 + num2)
sub = int(num1 - num2)
mult = int(num1 * num2)
div = int(num1 / num2)
expo = int(num1 ** num2)

#Imprimir os resultados na "console"

print(f'A soma de {num1} e {num2} é igual a {soma}.')
print(f'A subtração de {num1} e {num2} é igual a {sub}.')
print(f'A multiplicação de {num1} e {num2} é igual a {mult}.')
print(f'A divisão de {num1} e {num2} é igual a {div:.2f}.')
print(f'A exponenciação de {num1} e {num2} é igual a {expo}.')
