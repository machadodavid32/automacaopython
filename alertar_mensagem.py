# Alertar e pedir informação no Pyautogui

import pyautogui

pyautogui.alert(text='Iniciando sua automação', title='Automação de login', button='ok')

"""
# Pedir informação
email = pyautogui.prompt(text='Digite seu email', title='Informações obrigatórias')
print(f'Você digitou {email}')

# Resposta: Após abrir a caixinha pra colocar o email, a resposta chega no terminal
# Você digitou machadodavid32@gmail.com


# Confirmar se algo deve acontecer ou não

resposta = pyautogui.confirm(text='Continuar rodando essa automação?', title='Confirmação',
buttons=['sim','não','cancelar'])

if resposta == 'sim':
    print('Continuando automação')
elif resposta == 'não':
    print('Encerrando automação')
else:
    print('Operação cancelada')

"""

# Criando uma caixa com a senha aparecendo como ********

senha = pyautogui.password(text='Digite sua senha: ', title='dados de login', mask='*')
print(senha)
# A resposta será impressa no terminal após digitar a senha na caixa

