salario = float(input('Qual é o salário do funcionario? R$'))
novo = salario + (salario * 0.15)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f}.'.format(salario, novo))