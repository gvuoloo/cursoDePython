#Desaio 17

#Para este desafio, peça ao usuário para digitar a sua idade. Se a idade for menor que 13, imprima "Você é uma criança". Se a idade estiver entre 13 e 19, "Você pe um adolescente". Se a idade for 20 ou maior, "Você é uma adulto".

idade = int(input('Insira a sua idade:'))
if idade < 13:
    print("Você é uma criança.")
elif 13 <= idade < 20:
    print("Você é um/a adolescente.")
else:
    print('Você é um/a adulto/a.')
