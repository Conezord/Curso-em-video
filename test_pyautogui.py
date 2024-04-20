import pyautogui

#pausa entre cada linha, usar para setar uma pausa "global"
pyautogui.PAUSE = 0.5

print(pyautogui.position())
pyautogui.moveTo(x=1200, y=200)

#usado para criar uma pausa apenas nesse exato momento
pyautogui.sleep(2)

#ambos comandos a seguir fazem a mesma coisa
#apenas facilita a leitura colocando qual botão na função

#pyautogui.rightClick()
#pyautogui.click(button='right') 

#para localizar um print na tela ao inves da posição
# nome_da_variavel = pyautogui.locateonscreen("nome do arquivo")
botao_youtube = pyautogui.locateOnScreen('botaoyoutube.JPG')