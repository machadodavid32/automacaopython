"""
Projeto para buscas na olx
Navegar até o site
Encontrar os titulos
Encontrar os preços
Encontrar os links dos anuncios
Guardar os dados em um arquivo.csv
Fazer isso para todas as paginas existentes

"""

from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
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
# Navegar até o site
driver.get('https://sp.olx.com.br/sao-paulo-e-regiao/autos-e-pecas/motos?q=yamaha%20mt03')

while True:

    # Carregar todos os elementos da tela movendo até o final da página e depois ao topo
    sleep(10)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # descendo
    sleep(2)


    # Encontrando os titulos
    titulos = driver.find_elements(By.XPATH, "//div[@class='sc-12rk7z2-7 kDVQFY']//h2")

    # Encontrando os preços
    precos = driver.find_elements(By.XPATH, "//span[@class='m7nrfa-0 eJCbzj sc-ifAKCX ANnoQ']")

    # Encontrando os links
    links = driver.find_elements(By.XPATH, "//a[@data-lurker-detail='list_id']")

    # Guardar isso em um arquivo .csv
    for titulo, preco, link in zip(titulos, precos, links):
        with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
            link_processado = link.get_attribute('href')
            arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')
    # os.linesep -> Quebra de linha para que as informações na tabela fiquem organizadas
    try:
        botao_proxima_pagina = driver.find_element(By.XPATH, "//span[text()='Próxima pagina']")
        sleep(2)
        botao_proxima_pagina.click()
    except:
        print('Chegamos na ultima pagina')
        break    


input('')
driver.close()