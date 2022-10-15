import pyautogui
from time import sleep

""" Como simular rolagem do mouse

pyautogui.moveTo(1470, 571, duration=2)

for i in range(500):
    pyautogui.scroll(-1500)  # Aqui faz a rolagem para baixo. Se colocar sem o sinal de negativo, faz a rolagem para cima.
    sleep(2)  # Para dar tempo de carregar, por exemplo, uma pagina.
    """

pyautogui.moveTo(1264,347, duration=1) 
pyautogui.scroll(-2500)

# acima foi uma automação para chegar no tópico 'historia' da pagina da wiki https://pt.wikipedia.org/wiki/Brasil

