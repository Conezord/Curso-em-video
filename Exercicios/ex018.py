#sen, cos e tg de um angulo
import math
an = float(input('Digite o ângulo que você deseja saber sen, cos e tg: '))
anrad = math.radians(an)
sen = math.sin(anrad)
cos = math.cos(anrad)
tg = math.tan(anrad)
print('O ângulo de {:.2f}º tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(an, sen, cos, tg))