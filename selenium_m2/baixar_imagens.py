from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # Serve para trabalhar com dropdown
import os, random


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

"""
driver.get('https://pt.wikipedia.org/wiki/Brasil')
sleep(1)

# Abaixo, estamos encontrando uma imagem e baixando ela.
bandeira = driver.find_element(By.XPATH, "//img[@alt='Bandeira do Brasil']")

with open('bandeira.jpg', 'wb') as arquivo:
    arquivo.write(bandeira.screenshot_as_png)



# Abaixo, vamos selecionar mais de uma imagem de um site e extrair todas.
# É só achar algo em comum.

"""
driver.get('https://cursoautomacao.netlify.app/')
sleep(1)
driver.execute_script("window.scrollTo(0, 2100);")
sleep(2)
imagens = driver.find_elements(By.XPATH, "//img[@class='img-thumbnail']")
contador = 1
for imagem in imagens:
    with open(f'imagem{contador}.jpg', 'wb') as arquivo:
        arquivo.write(imagem.screenshot_as_png)
        sleep(1)
    contador += 1    

input('')
driver.close()

