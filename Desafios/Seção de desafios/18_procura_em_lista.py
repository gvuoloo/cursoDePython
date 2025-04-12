#Desafio 18

#Para este desafio, imagine que você tem uma loja de carros. Crie uma lista com os carros que você tem em estoque: BMW X6, BMW i5, BMW i8.
#Peça ao usuário para que ele insira o nome do carro que deseja comprar. Se o carro estiver em estoque, imprima "Este caro está disponível". Se o carro não estiver em estoque, imprima: "Desculpe, este carro não está disponível".


carro_estoque = ['BMW X6', 'BMW i5', 'BMW i8']

carro_desejado = input('Insira qual o modelo do carro que você busca:')
if carro_desejado in carro_estoque:
    print('Este caro está disponível.')
else:
    print('Desculpe, este carro não está disponível.')