import pyautogui
from time import sleep


"Aqui vamos utilizar as teclas de atalho do teclado, como por exemplo, tab, para acessar um campo com email e senha"

pyautogui.click(1235,455, duration=1)
sleep(1)
pyautogui.typewrite('machadodavid32@gmail.com')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.typewrite('122345')
sleep(1)
pyautogui.press('tab')
pyautogui.press('space')

# Para ver todas as teclas que são usadas no press, digite:
print(pyautogui.KEYBOARD_KEYS)

# Como usar combinações de teclas
pyautogui.click(15468, 984, duration=2)
pyautogui.keyDown('ctrl')  # Aqui ele está segurando uma tecla crtl
pyautogui.keyDown('a')  # Aqui ele está segurando as duas teclas juntas, ctrl e a (crtl + a = selecionar todo o texto)
pyautogui.keyUp('ctrl')  # Soltando a tecla
pyautogui.keyUp('a')  #  Soltando a outra tecla

# Agora um modo mais facil de usar a combinação
pyautogui.hotkey('ctrl', 'a')

# Da pra usar coom ctrl c, ctrl v, etc...


