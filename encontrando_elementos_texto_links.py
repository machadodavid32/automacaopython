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


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

link_home = driver.find_element(By.LINK_TEXT, 'Home')  # Aqui estamos localizando um elemento pelo texto do link 'home' no codigo do site acima
link_desafio = driver.find_element(By.PARTIAL_LINK_TEXT, 'Des') # Aqui estamos procurando por um texto parcial, não sendo necessario escrever toda a palavra

# Abaixo, vamos fazer uma condicional para verificar se os elementos foram encontrados

if link_home is not None:
    print('Encontrado o link')

if link_desafio is not None:
    print('Encontrado os links do menu')

input(' ')

driver.close