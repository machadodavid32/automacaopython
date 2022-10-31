"""
Neste aqui teremos como saber como alguns campos estão habilitados ou não

"""

from cgitb import enable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

"""
Para esta aula, precisamos ir até um site, digitar f12 no teclado e clicar dentro da tela de codigo. 
Após isso, apertar 'crtl f' que vai abrir um campo de busca. Neste campo digite: //*[text()='Escreva aqui o texto']

VEJA NA LINHA 36 O EXEMPLO
"""


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios.html')

botao1 = driver.find_element(By.ID, 'btn1')  # Aqui estamos localizando um elemento ...
botao2 = driver.find_element(By.CLASS_NAME, 'btn2 btn btn-dark')
# botao3 = driver.find_element(By.CLASS_NAME, 'btn2 btn btn-warning')

# Abaixo, vamos fazer uma condicional para verificar se os elementos foram encontrados

if botao1 is enable():
    print('Campo está habilitado')

else:
    print('Campo desabilitado')

if botao2 is enable():
    print('Campo habilitado')

else:
    print('Campo desabilitado')

input(' ')

driver.close()