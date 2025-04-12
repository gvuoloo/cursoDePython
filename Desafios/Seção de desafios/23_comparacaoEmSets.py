#Desafio 23

#Para este desafio, crie dois conjuntos, cada um contendo 5 nomes de seus amigos. Alguns nomes devem estar presentes em ambos os conjuntos. Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado.

amigos1 = {'Gabriela', 'Eduardo', 'Gabriel', 'Luisa', 'Sibene'}
amigos2 = {'Vitória', 'Diogo', 'Lucas', 'Luisa', 'Gabriela'}

print(amigos1.intersection(amigos2))

#ou da seguinte forma:

result = amigos1.intersection(amigos2)
print(result)