from _random import choice

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
minha_lista = [aluno1, aluno2, aluno3, aluno4]
escolha = choice(minha_lista)
print('O aluno escolhido foi {}.'.format(escolha))