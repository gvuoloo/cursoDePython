#Desafio 14

#Criar um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando o comando "break". Em seguida, crie um segundo loop que imprima os números de 1 a 10, mas pule a impressão do número 5 usando o comando "continue".

num = 0
print('Para o desafio utilizando o break para pular o número 5:')
for num in range (1, 11):
    if num == 5:
        break
    print(num)

#para o break em 5
# \n serve como "line break. Um espaçamento para deixar mais bonito na impressão, que utilizei no print abaixo

print('\nPara o desafio utilizando o continue para pular o número 5:')
for num in range(1, 11):
    if num == 5:
        continue
    print(num)