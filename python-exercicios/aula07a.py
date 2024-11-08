n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
d = n1 / n2
m = n1 * n2 
di = n1 // n2
e = n1 ** n2

print('A soma é {}.\nA divisao é {:.2f}.\nA multiplicacao é {}.\nA divisao inteira é {}.\nA exponenciação é {}.'.format(s, d, m, di, e), end='')
print('teste')