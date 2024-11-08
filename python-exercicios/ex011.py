largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar a sua parede, você precisará de {}L de tinta.'.format(tinta))