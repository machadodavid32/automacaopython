"""O Wait implicito vai aguardar o elemento aparecer na tela para evitar o erro quando,
por exemplo, o sistema vai clicar e o elemento a ser clicado ainda não apareceu. """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


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
driver.implicitly_wait(10) # Vai aguardar por dez segundos até o elemento ficar visivel
driver.get('http://google.com/flights')

sugestoes_de_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz']")

sugestoes_de_voo[0].click()
input('')
driver.close()