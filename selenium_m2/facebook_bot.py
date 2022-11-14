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


# Passos para automação Facebook



# Clicar em login
# Encontrar e clicar no campo de postagem
# Clicar dentro do campo de status
# Digitar algo
# Clicar em publicar

driver = iniciar_driver()
# Abrir página facebook.com
driver.get('https://facebook.com')
sleep(2)

# Digitar email
email = driver.find_element(By.ID, 'email')
sleep(2)

# Digitar senha
senha = driver.find_element(By.ID, 'pass')



input('')
driver.close()
