"""
radiobutton é quando vc pode selecionar apenas uma opção na caixinha do formulario

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
driver.get('https://cursoautomacao.netlify.app/')

# Navegar até o site
driver.get('https://cursoautomacao.netlify.app/')
sleep(1)
linux_radio_button = driver.find_element(By.ID, 'LinuxRadioButton')
# if linux_radio_button.is_selected() == True:
#     print("Botão já selecionado")

linux_radio_button.click() # Aqui vai clicar no botoão linux
sleep(2)
radios = driver.find_elements(By.XPATH, "//input[@type='radio']") # já este vai achar as três opções
# para clicar no elemento certo, vc pode usar o indexador correto, conforme abaixo:
radios[1].click()

input('')
driver.close()

