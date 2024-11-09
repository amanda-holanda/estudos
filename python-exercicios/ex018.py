from math import cos, sin, tan, radians
n = float(input('Digite um angulo qualquer: '))
radiano = radians(n)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print('O valor do angulo {} seno é {:.2f}, do seu cosseno é {:.2f} e da sua tangente é {:.2f}.'.format(radiano, seno, cosseno, tangente))