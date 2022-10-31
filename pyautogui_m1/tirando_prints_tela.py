# Como tirar print da tela inteira ou parte dela
import pyautogui

pyautogui.screenshot('teste.jpg')  # tira print da tela atual (toda). 

# Abaixo, vamos usar o mouseInfo() para definir os pontos a serem recortados.

# Assm, vc coloca o o primeiro parametro e aperta f6, depois o segundo parametro é ..
# ..para direita e o terceiro parametro é para baixo. Abaixo:

pyautogui.screenshot('parte.jpg', region=(1824,355, 500, 410))

# A sequencia acima é ponto principal = 1824,355, indo pra dieira = 500, indo pra baixo = 410

