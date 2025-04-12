#Desafio 12

#Para este desafio, crie uma lista de frutas e outra de vegetais. Use um "for loop" aninhado (nested for loop) para imprimir todas as combinações possíveis de frutas e vegetais, com a furta primeiro e o vegetal em segundo.


frutas = ['abacate', 'abacaxi', 'morango']
vegetais = ['alface', 'brócolis', 'couve']

# Loop externo: percorre cada fruta
for fruta in frutas:
    # Loop interno: para CADA fruta, percorre todos os vegetais
    for vegetal in vegetais:
        print(f"{fruta} + {vegetal}")  # Imprime a combinação
