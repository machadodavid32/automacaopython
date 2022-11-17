"""Como lidar com iframe

Iframes são páginas dentro de páginas, que inclusive tem scrolls

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
driver.execute_script("window.scrollTo(0, 2400);")
sleep(2)

# Para entrar num iframe, o correto é achar o iframe com o botão f12 no site.
iframe = driver.find_element(By.XPATH, " //iframe[@src='https://cursoautomacao.netlify.app/desafios.html']")
sleep(2)

# Depois de encontrar o iframe, vamos entrar dele dela com
driver.switch_to.frame(iframe)
sleep(2)

# Interagindo com o iframe - mesma coisa, com f12
campo_nome = driver.find_element(By.ID, "dadosusuario")
sleep(2)
campo_nome.send_keys('David')
sleep(1)

# agora vamos sair do Iframe
driver.switch_to.default_content()

input ('')
driver.close()

