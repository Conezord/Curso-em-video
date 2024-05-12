#conversor de temperaturas

celsius = float(input('Qual a temperatura em ºC? '))
farenheit = ((9 * celsius)/5) +32
#pode ser com ou sem parenteses no farenheit por causa da ordem de precedencia

print('A temperatura de {0}ºC corresponde à {1}ºF'.format(celsius, farenheit))