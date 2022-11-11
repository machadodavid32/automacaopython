from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # Serve para trabalhar com dropdown
from selenium.webdriver.common.keys import Keys  # serve para utilizar as teclas do teclado na automação

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

driver.get('https://cursoautomacao.netlify.app/')
sleep(1)

botao_windows = driver.find_element(By.ID, "WindowsRadioButton")
botao_windows.click()
botao_windows.send_keys(Keys.DOWN)  # aqui ele vai descer no botão abaixo do site.
# Da pra usar tab, tecla pra cima, pra frente, etc; Depende do site.


input('')
driver.close()

