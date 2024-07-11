# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamaanho em metros quadrados da area a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

area = input('Olá. Escreva o tamanho em metros quadrados da área a ser pintada: ')

#em reais
preco_lata = 80
#em litros
medida_lata = 18

#quantidade de litros necessarios
qntdd_litro = int(area)/3

#qutdde de latas
qntdd_lata = int(qntdd_litro/medida_lata)

#valor total
total = int(qntdd_lata*preco_lata)

print(f'Será necessário {qntdd_lata} latas e custará {total} reais.')
