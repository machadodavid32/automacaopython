import pyautogui
from time import sleep

#pyautogui.moveTo(1776,22, duration=2)

# pyautogui.move(50, 20, duration=2)  # Aqui significa (50, 0) -> 50 é o eixo X e 0 eixo Y. 

# Eixo X = negativo vai para esquerda. Ex. -50. Positivo vai para direito
# Eixo Y - Vai para cima e para baixo, onde para cima é negativo
#for n in range(100):  # Exemplo do jogo
#    sleep(0.5)  # segundos entre um click e outro click
#    pyautogui.click()

# Posição algo - use o mouse info (abra o terminal e faça o processo pra abertura)

# Fazer algo com essa posição
pyautogui.moveTo(991,1043, duration=2)
pyautogui.click()
pyautogui.moveTo(1047,380, duration=2)
pyautogui.click()
pyautogui.moveTo(705,479, duration=2)
pyautogui.click()
pyautogui.moveTo(589,452, duration=2)
pyautogui.click()
for c in range(100):
    sleep(0.5)
    pyautogui.click()