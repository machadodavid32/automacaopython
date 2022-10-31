from turtle import left
import pyautogui

# nova pasta windows 11
pyautogui.moveTo(903,1053, duration=1)  # até a pasta central
pyautogui.click()
pyautogui.moveTo(132,384, duration=1) # lado esquerdo, disco d:
pyautogui.click()
pyautogui.moveTo(788,541, duration=1) # indo para dentro da pasta (d:)
pyautogui.click(button='right') # abrindo menu dentro da pasta
pyautogui.moveTo(820, 745, duration=1) # descendo para opção 'novo'
pyautogui.click()
pyautogui.moveTo(1250, 745, duration=1) # indo para o submenu a esquerda
pyautogui.moveTo(1250, 330, duration=1) # subindo indo para opção 'nova pasta'
pyautogui.moveTo(1300, 331, duration=0.1) # fixaando o ponteiro do mouse em 'nova pasta
pyautogui.doubleClick() # criando nova pasta


