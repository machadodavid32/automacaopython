from msilib import MSIMODIFY_DELETE
from turtle import left, right
import pyautogui


# Click personalizado
pyautogui.click(x=1000, y=500, clicks=2, interval=0.0, button=left, duration=2)

# x = posição na horizontal
# y = posição na vertical
# clicks = igual ao número de clicks
# interval = é o tempo entre os clicks
# button = qual dos botões do mouse (esquerdo = left, direito = righ, meio = middle)
# duration = velocidade do mouse pra chegar no destino


# click na posição atual (com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')


# Funções prontas para click
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()

