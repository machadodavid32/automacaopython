"""
Vamos usar como exemplo o site de testes e vamos efetuar um login com usuario e senha

Os primeiros passos é saber como fazer, passo a passo:

Abrir o site - https://cursoautomacao.netlify.app/desafios.html
Procurar o campo 'Digite seu nome no campo abaixo'
Procurar o botão 'clique aqui'
Clicar no botão 'Clique aqui

Clicar no campo 'Enter senha'
Digitar a senha

Clicar em 'Enviar'


"""

from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1080,900', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(1)
driver.execute_script("window.scrollTo(0, 1650);")
sleep(2)

carros = driver.find_elements(By.XPATH, "//input[@name='carros']")
carros[1].click()
carros[3].click()
carros[4].click()

motos = driver.find_elements(By.XPATH, "//input[@name='motos']")

for moto in motos:
    moto.click()

input('')
driver.close()

# Neste exercicio, precisei aumentar a resolução da página para funcionar pois o campo...
# ... "Clique aqui" não estava visivel na pagina
# Mas eu poderia também rolar para baixo.
