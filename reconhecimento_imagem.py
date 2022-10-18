import pyautogui

# Encontrar as coordenadas próximas de onde a imagem está
print(pyautogui.locateOnScreen('cal.png'))

# reconhece poucas cores na tela. É possivel da seguinte forma, vc escolhe uma imagem simples...
# e salva essa imagem como nome.png. Depois vc executa os comandos pra localização.


print(pyautogui.locateCenterOnScreen('cal.png'))


