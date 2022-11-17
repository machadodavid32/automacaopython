"""Ações com o mouse - clicar com o botão direito e descer e clicar em, por exemplo, copiar e colar.

"""

from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os, random
from selenium.webdriver import ActionChains  # para clique botão direito do mouse
from selenium.webdriver.common.keys import Keys  # para descer ou subir as opções após botão direito do mouse

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
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')
sleep(1)

botao = driver.find_element(By.ID, "botao-direito")
chain = ActionChains(driver)
chain.context_click(botao).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform() 
# Vai clicar com o botão direito com pausa de 3 segundos ..e vai descer com a tecla para baixo até quantas vezes eu quiser.

# OBS - PARA FAZER UM NOVO CLIQUE, É NECESSÁRIO REFAZER O PROCESSO ACIMA PARA OUTRO PARTE DA PAGINA, igual abaixo

driver.get('https://cursoautomacao.netlify.app')
sleep(1)

window_10_radio_button = driver.find_element(By.ID, 'WindowsRadioButton')
chain2 = ActionChains(driver)
chain.context_click(window_10_radio_button).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform() 



input ('')
driver.close()
