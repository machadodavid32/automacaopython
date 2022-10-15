import pyautogui

"""
Arrastando coisas para outro lugar
"""
for n in range(4):
    pyautogui.moveTo(1400,221, duration=1)  # indo até a pasta 1
    pyautogui.dragTo(1395, 650, button='left', duration=1) # Arrastando os 4 arquivos para o local desejado

# o codigo acima pode ser utilizado para arrastar varias coisas e pode usar um laço de repetição para todos