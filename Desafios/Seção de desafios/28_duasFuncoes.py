#Desafio 28

#Para este desafio, crie duas funções: 
# 
# 01
# A primeira deve aceitar um número e retornar o dobro desse número. 

def dobro(num):
    return num * 2

# 02
# A segunda função deve aceitar um número e retornar o quadrado desse número. 

def quadrado(num):
    return dobro(num) ** 2

# 03
# Em seguida, chame a primeira função dentro da segunda para retornar o quadrado do dobro de um número.

user_num = int(input('Digite um número: '))
print(f'O quadrado do dobro do número {user_num} é igual a {quadrado(user_num)}.')