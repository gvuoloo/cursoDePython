#Desafio 24

#Crie uma função que aceita um número como entrada e retona o quadrado desse número.

def quadrado(num): #para criar a função
    return num ** 2 # ** para colocar exponencial

num = float(input('Para calcularmos o valor de um número ao quadrado, insira aqui um número: '))

print(f'O valor ao quadrado de {num:.2f} é: {quadrado(num):.2f}.')