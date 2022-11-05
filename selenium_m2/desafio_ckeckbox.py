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
driver.get('https://cursoautomacao.netlify.app/desafios.html')

driver.execute_script("window.scrollTo(0,700)")
sleep(2)
conversivel = driver.find_element(By.ID, 'conversivelcheckbox')
off_road = driver.find_element(By.ID, 'offroadcheckbox') 
conversivel.click()
off_road.click()

input('')
driver.close()

