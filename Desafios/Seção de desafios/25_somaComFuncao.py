#Desafio 25

#Para este desafio, crie uma função que aceite dois números como entrada e retone a soma desses números.

def soma(x, y):
    return x + y

x = int(input('Insira aqui um valor para x: '))
y = int(input('Insira aqui um valor para y: '))

print(f'A soma de {x} + {y} é igual a: {soma(x, y)}.')