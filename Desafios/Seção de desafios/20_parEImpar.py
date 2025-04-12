#Desafio 20

#Crie uma lista de número de 1 a 10. use um 'for loop' para interar sobre a lista. Se o número atual da interação for par, imprima "O número [número] é par". Se o número for ímpar, "O número [número] é ímpar"

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num:
    if i % 2 == 0:
        print(f'O número {i} é par.')
    else:
        print(f'O número {i} é ímpar.') 
