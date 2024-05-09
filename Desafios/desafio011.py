larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

print('A área total da parede é de {} m²'.format(larg * alt))
print('Serão necessários {:.1f} litros de tinta para pintar a parede'.format(larg * alt / 2))