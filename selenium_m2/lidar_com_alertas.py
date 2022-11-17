"""Lidar com alertas - alertas são aquelas informações que aparecem num quadro a parte da tela, tipo para confirmar algo.


"""

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
sleep(1)

# Descer a página
driver.execute_script("window.scrollTo(0, 600);")
sleep(2)

# Primeira situação, vamos clicar em alerta

campo_nome = driver.find_element(By.ID, "nome")
sleep(1)
campo_nome.send_keys("david")
sleep(1)

botao_alerta = driver.find_element(By.ID, "buttonalerta")
sleep(1)
botao_alerta.click()
alerta1 = driver.switch_to.alert  # Vai acionar o alerta da página
sleep(1)
alerta1.accept() # Vai clicar no ok para fechar o alerta
sleep(1)

# Segunda situação, escrever o nome e clicar em ok ou cancelar 

botao_confirmar = driver.find_element(By.ID, "buttonconfirmar")
sleep(1)
botao_confirmar.click()
alerta2 = driver.switch_to.alert  # Vai acionar o alerta da página
sleep(1)
alerta2.accept() # Vai clicar no OK para fechar o alerta
# alerta2.dismiss() # Aqui vai clicar EM CANCELAR
sleep(1)

# Terceira situação, inserir dados ou clicar em confirmar ou cancelar, além de fechar o alerta posterior

botao_fazer_pergunta = driver.find_element(By.ID, "botaoPrompt")
sleep(1)
botao_fazer_pergunta.click()
sleep(1)
alerta3 = driver.switch_to.alert
sleep(1)
alerta3.send_keys('David') # escrevendo
sleep(2)
alerta3.accept() # vai confirmar o envio
sleep(2)
alerta3.dismiss() # vai fechar a janela posterior




input ('')
driver.close()
