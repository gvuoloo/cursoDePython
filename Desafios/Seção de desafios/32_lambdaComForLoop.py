#Desafio 32

#01
# Crie uma função lambda que eleve um número ao quadrado.

quadrado = lambda x: x ** 2

#02
#Em seguida, use essa função para calcular o quadrado de todos os números em uma lista usando um loop for.

lista = [1, 2, 3, 4, 5, 6]

resultados = [] #uma lista vazia para que todos os resultados entrem nela

for i in lista: #o for loop
    resultados.append(quadrado(i))


print(f'Os quadrados dos números {lista} são {resultados}.')