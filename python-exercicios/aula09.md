> Manipulando texto

1) Fatiamento: A contagem começa sempre do índice zero.
- Ex: frase = 'Curso em Video Python'
  - print(frase[0]) == 'C'
  - print(frase[9:]): vai mostrar do caractere 9 até o final
  - print(frase[9::3]) == Veph

2) função len(): mostra o tamanho da string, a qntdd de caracteres
- Ex: len(frase) == 21

3) função count(): mostra quantas vezes uma letra existe numa string. 
- Ex: frase.count('o') == 3
    Você pode fazer o fatiamento tbm usando o count. 
- Ex: frase.count('o', 0, 13): retorna a quantidade de vezes que aparece o 'o' entre o indice 0 e 13.

4) find('deo'): mostra o índice de onde COMEÇOU o 'deo'.
- Ex: frase.find('deo') == 11
Caso você procure uma sring que não existe dentro da frase, ele retorna -1.
- Ex: frase.find('Android') == -1

5) Operador in: retorna True or False para verificar se aquela string existe ou não dentro da frase.
- Ex: 'Curso' in frase == True

> Transformação de texto
1) replace()
- Ex: frase.replace('Python','Android') == 'Curso em Video Android'
2) upper()
- Ex: frase.upper() == 'CURSO EM VIDEO PYTHON'
3) lower()
- Ex: frase.upper() == 'curso em video python'
3) capitalize()
- Ex: frase.capitalize() == 'Curso em video python'
4) title()
- Ex: frase.title() == 'Curso Em Video Python'
Para os exemplos abaixo: frase = '  Aprendendo em Python  '
5) strip()
- Ex: frase.strip() == 'Aprendendo em Python'
6) rtrip() - r significa right
- Ex: frase.rstrip() == '  Aprendendo em Python'
7) ltrip() - l significa left
- Ex: frase.lstrip() == 'Aprendendo em Python  '

> Divisão