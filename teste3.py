import pyautogui

for n in range(5):
    pyautogui.moveTo(1768,999, duration=2)
    pyautogui.click()
    pyautogui.typewrite('Essa mensagem foi criada através de automação Python - teste - e vai se repetir 5x')
    pyautogui.moveTo(2512,997, duration=2)
    pyautogui.click()
