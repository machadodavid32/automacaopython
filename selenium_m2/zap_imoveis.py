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
driver.get('https://www.zapimoveis.com.br/')
sleep(5)
# Clicar em qual tipo de imovel
qual_tipo = driver.find_element(By.XPATH, "//input[@label='Qual tipo?']")
qual_tipo.click()
sleep(2)
clique_fora = driver.find_element(By.CLASS_NAME, 'new-hero__content-wrapper')
clique_fora.click()
onde = driver.find_element(By.XPATH, "//input[@label='Onde?']")
onde.click()