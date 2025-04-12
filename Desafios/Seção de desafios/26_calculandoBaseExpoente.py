#Desafio 26

#Para este desafio, crie uma função que calcule a potência de um número. A função deve aceitar dois argumentos: a base e o expoente. No entanto, se o expoente não for fornecido ao chamar a função, ele deve assumir o valor padrão de 2.

def potencia(base, expo=2):
    return base ** expo

user_base = int(input('Insira um número para calcular a exponenciação: '))
user_expo = (input('Insira a quantas vezes gostaria de elevar o número: ')) #não está em 'int' para evitar que, caso não seja inserido um número, vá como 0.

if user_expo: #caso seja verdadeiro e o usuário tenha inserido um valor para a exponencial.
    print(f'O resultado é: {potencia(user_base, int(user_expo))}.')
else:
    print(f'O resultado é: {potencia(user_base)}.') #não precisa chamar a segunda variável porque ele já vai considerar que o segundo é = 2.
