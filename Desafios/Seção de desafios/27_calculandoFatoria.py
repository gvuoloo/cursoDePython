#Desafio 27

#As funções recursivas são funções que se chamam dentro do seu próprio bloco de código. Elas são úteis para resolver problemas que podem ser divididos em problemas menores de natureza semelhante.

#Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial de um número. O fatorial de um número N é o produto de todos os números inteiros positivos de N até 1.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

user_num = int(input('Digite um número: '))

print(f'O fatorial de {user_num} é de {fatorial(user_num)}.')