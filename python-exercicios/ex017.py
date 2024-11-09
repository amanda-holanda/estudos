from math import sqrt, pow, hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hip = sqrt(pow(n1,2)+pow(n2,2))
hip2 = hypot(n1, n2)
print('O comprimento da hipotenusa desse triangulo retangulo é {} e {}'.format(hip, hip2))