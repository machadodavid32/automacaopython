import pyautogui
import pyperclip  # para caracteres especiais na nossa lingua

"""Como digitar em qualquer lugar"""

"""
# o codigo abaixo não reconhece caracteres especiais.

for i in range(50):
    pyautogui.moveTo(1535,988, duration=2)
    pyautogui.click()
    pyautogui.typewrite('Essa é uma mensagem enviada de um bot criado por David')
    pyautogui.moveTo(1840,988, duration=1)v
    pyautogui.click()
"""

# para reconhecer caracteres especiais, vamos criar uma função

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('crtl', 'v')

pyautogui.moveTo(1843,154, duration=2)
pyautogui.doubleClick()
pyautogui.moveTo(1241,364, duration=1)
escrever_frase('Olá, boa noite!')






