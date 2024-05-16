# ler o comprimento do cateto oposto e adjacente
# e calcule e mostre o comprimento da hipotenusa
from math import sqrt, pow

catop = float(input('Cateto oposto: '))
catadj = float(input('Cateto adjacente: '))
hipotenusa = sqrt(pow(catop, 2) + pow(catadj, 2))

print('Cateto oposto é {:.0f}, cateto adjacente é {:.0f} e a hipotenusa é {:.0f}.'.format(catop, catadj, hipotenusa))