#Desafio 15

#Crie uma lista de frutas que inclui "maçã" 3 vezes e outras frutas de sua escolha. Use o loop for para contar quantas vezes "maçã" aparece na lista e imprima o resultado.

frutas = ['maçã', 'banana', 'pequi', 'maçã', 'bocaiúva', 'abacaxi', 'maçã']

contador_macas = 0

for fruta in frutas:
    if fruta == 'maçã':
        contador_macas += 1

print(f'Existem {contador_macas} maçãs na lista de frutas.')