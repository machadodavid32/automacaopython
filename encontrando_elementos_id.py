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

botao = driver.find_element(By.ID, 'btn1')  # Aqui estamos localizando um elemento pelo ID  buttonalerta no codigo do site acima

# ou podemos localizar uma lista de elementos, conforme abaixo
botoes = driver.find_elements(By.ID, 'buttonalerta')

# Abaixo, vamos fazer uma condicional para verificar se os elementos foram encontrados

if botao is not None:
    print('Botão encontrado')

if botoes is not None:
    print('Botões encontrados')

input(' ')

driver.close