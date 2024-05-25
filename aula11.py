'''Cores no terminal
ANSI - escape sequence - começar com contrabarra e um codigo
padrão = codigo \033['style';'text';'background'm
exemplo: \033[0;33;44m]
style = 0, 1, 4 ou 7
text = 30 a 37
back = 40 a 47
'''

print('\033[4;31mOlá, Mundo!')