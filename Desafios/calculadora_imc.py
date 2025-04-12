# Cálculo de IMC
'''
O Índice de Massa Corporal (IMC) é calculado da seguinte maneira:
Divisão entre o peso em quilogramas (kg) pela altura ao quadrado em metros (m²). 
'''
#Onde o resultado significa o seguinte:
peso = float(input('Para calcular o seu Índice de Massa Corporal, por favor, insira o seu peso, em quilos: '))

altura_cm = float(input('Insira a sua altura, em centímetros: '))

altura_m = altura_cm / 100

imc = peso / (altura_m ** 2)

if imc < 18.5:
    print(f'Cuidado. O seu IMC é de {imc:.2f}. Você está abaixo do seu peso ideal.')
elif 18.5 <= imc < 24.9:
    print(f'Parabéns! O seu IMC é de {imc:.2f}. Você está dentro do seu peso ideal.')
elif 25 <= imc <39.9:
    print(f'Atenção. O seu IMC é de {imc:.2f}. Você está obeso.')
else:
    print(f'Cuidado. O seu IMC é de {imc:.2f}. Você está com obesidade grave.')