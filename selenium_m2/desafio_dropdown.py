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
driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(2)

driver.execute_script("window.scrollTo(0, 2050);")
sleep(3)

paises = driver.find_element(By.XPATH, "//select[@id='paisesselect']")
opcoes = Select(paises)
# O comando acima vai acessar as trÊs opções de paises que o dropdown apresenta. Temos três forma de escolher:

opcoes.select_by_value('estadosunidos')
sleep(2)
opcoes.select_by_value('africa')
sleep(2)
opcoes.select_by_value('chille')
sleep(2)

"""
# por indice
opcoes.select_by_index(1)
sleep(2)
# por value
opcoes.select_by_value('estadosunidos')
sleep(2)
opcoes.select_by_visible_text('Brasil')
"""

input('')
driver.close()