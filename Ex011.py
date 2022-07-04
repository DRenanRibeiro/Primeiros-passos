largura = float(input('Largura da parede em metros:'))
altura = float(input('Altura da parede em metros:'))
mão = int(input('Quantas  mãos de tinta:'))
área = largura * altura 
tinta = (área / 2) * mão
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².' .format(largura, altura, área))
print('Para pintar essa parede, você precisará de {}l de tinta.' .format(tinta))