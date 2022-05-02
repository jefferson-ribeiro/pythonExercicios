lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = lar * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}mx{}m e su area é de {:.2f}m2. Para pintar essa parede, '
      'você presisará de {:.2f}l de tinta.'.format(lar, alt, area, tinta))
