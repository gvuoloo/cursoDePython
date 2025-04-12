# Desafio com 'Sets'

'''
Criar um progarma que gere 3 listras de acordo com a necessidade logo abaixo:

Lista 1 = Funcionários que têm carro e trabalham à noite;
Lista 2 = Funcionários que têm carro e trabalham durante o dia;
Lista 3 = Funcionários que não têm carro.
'''
funcionarios = {'Eduardo', 'Silbene', 'Vitória','Gustavo', 'Diogo', 'Luisa', 'Lucas', 'Camila', 'Gabriel'}
turno_dia = {'Silbene', 'Gustavo', 'Diogo', 'Luisa', 'Gabriel'}
turno_noite = {'Vitória', 'Eduardo', 'Lucas', 'Camila'}
tem_carro = {'Camila', 'Diogo', 'Eduardo', 'Gabriel'}

list1 = set(tem_carro).intersection(turno_noite)
print(f'Funcionários que têm carro e trabalham à noite são: {list1}.')

list2 = set(tem_carro).intersection(turno_dia)
print(f'Funcionários que têm carro e trabalham durante o dia: {list2}.')

list3 = set(funcionarios).difference(tem_carro)
print(f'Funcionários que não têm carro: {list3}.')