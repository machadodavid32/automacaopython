import email
import pyautogui

email = pyautogui.prompt(text='Informe seu email', title='Dados de login')
senha = pyautogui.password(text='Informe sua senha', title='Dados de login', mask='*')

pyautogui.click(1878,173, duration=2)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)


# O codigo acima vai pedir email e senha em uma caixa de dialogo e, após, as informações de..
# ...de email e senha serão coladas no bloco de notas ao lado

