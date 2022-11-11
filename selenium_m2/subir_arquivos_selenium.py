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
driver.get('https://cursoautomacao.netlify.app')
sleep(2)

driver.execute_script("window.scrollTo(0, 2100);")
sleep(2)

escolher = driver.find_element(By.XPATH, "//input[@id='myFile']")
sleep(1)
# Abaixo vamos informar o caminho do arquivo do computador
#PARA CAMINHOS colocar duas barras para funcionar. Não esquecer.
escolher.send_keys("C:\\Users\\macha\\Downloads\\curriculo_David_Machado.docx")
sleep(1)
enviar = driver.find_element(By.XPATH, "//input[@value='Enviar Arquivo']")
enviar.click()


input('')
driver.close()

