#Desafio com If, Elfi e Else

'''
Criar um programa que dependendo da temperatura (em celsius) do bife ele retornará o ponto de cozimento, em português. O usuário deverá fornecer a temperatura

Temperatudas - Cozimento
48°C - Selada
54°C - Ao ponto para mal passada
60°C - Ao ponto
65°C - Ao ponto para bem passada
71°C - Bem passada

'''

temp = int(input(f'Por favor, insira a temperatura do cozimento da carne, em graus Celsius: '))

if temp < 48:
    print('Será preciso cozinhar ou com uma temperatura mais alta, ou por mais tempo.')
elif 48 <= temp < 54:
    print('O ponto da sua carne será malpassado.')
elif 54 <= temp < 60:
    print('O ponto da sua carne será entre ao ponto a malpassado.')
elif 60 <= temp < 65:
    print('O ponto da sua carne será ao ponto.')
elif 65 <= temp < 71:
    print('O ponto da sua carne será de ao ponto para bem-passado.')
else:
    print('O ponto da sua carne será bem-passado.')