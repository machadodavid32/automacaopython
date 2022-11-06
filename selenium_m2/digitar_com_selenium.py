from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
driver.get('https://cursoautomacao.netlify.app/')

paragrafo = driver.find_element(By.XPATH, "//textarea[@placeholder='digite seu texto aqui']")
# paragrafo.send_keys('exemplo de texto')  # Obs: Usando este recurso, o texto é colocado de forma imediata no site, e pode dar ..
# ...problemas na automação. Então vamos fazer uma função

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)  # Aqui ele vai variar a digitação entre 1 e 5 segundos dividos por 30

digitar_naturalmente('teste', paragrafo)
#digitar_naturalmente('olá, isso é somente um teste')

input('')
driver.close()