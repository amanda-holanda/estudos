variavel = input('Digite algo: ')
tipo = type(variavel)
espaco = variavel.isspace()
numero = variavel.isnumeric()
alfabetico = variavel.isalpha()
maiuscula = variavel.isupper()
minuscula = variavel.islower()
capitalizada = variavel.istitle()

print('O tipo dessa querida é {}. Só tem espaços? {}. É um número? {}. É alfabetico? {}. Maiuscula? {}. Minuscula? {}. '.format(tipo, espaco, numero, alfabetico, maiuscula, minuscula))
print('Esta capitalizada? {}'.format(capitalizada))