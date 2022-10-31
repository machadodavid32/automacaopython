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
driver.get('https://cursoautomacao.netlify.app/')

titulo = driver.find_element(By.XPATH, '//*[text()="ZONA DE TESTES"]')  # Aqui estamos localizando um elemento ...
# ... pelo texto utilizando //*[text()='ZONA DE TESTES']

# Abaixo, vamos fazer uma condicional para verificar se os elementos foram encontrados

if titulo is not None:
    print(titulo.text)


input(' ')

driver.close()