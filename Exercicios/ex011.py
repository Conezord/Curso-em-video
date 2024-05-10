# pintando parede

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt

print('Sua parede tem dimensão de {:.1f}x{:.1f} e sua área é de {}m².'.format(larg, alt, (area)))
print('Para pintar essa parede, você precisará de {:.1f}L de tinta.'.format((area)/2))