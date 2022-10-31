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

titulo_do_site = driver.find_element(By.TAG_NAME, 'h1')  # Aqui estamos localizando um elemento ...
# ... via tag h1

elementos_h4 = driver.find_elements(By.TAG_NAME, 'h4') # Achando varios elementos

# Abaixo, vamos fazer uma condicional para verificar se os elementos foram encontrados

if titulo_do_site is not None:
    print('Encontrei o titulo do site')

if elementos_h4 is not None:
    print('Encontrei os elementos h4')


input(' ')

driver.close()