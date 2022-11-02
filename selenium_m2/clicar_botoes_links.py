"""
Vamos usar como exemplo o site de testes e vamos efetuar um login com usuario e senha

Os primeiros passos é saber como fazer, passo a passo:

Abrir o site - https://cursoautomacao.netlify.app/

Clicar em 'login'

Clicar no campo 'digite seu email'
Digitar email

Clicar no campo 'Enter senha'
Digitar a senha

Clicar em 'Enviar'


"""

from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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
botao_login = driver.find_element(By.LINK_TEXT, 'Login')
sleep(2)
botao_login.click()  # Primeira forma de clickar
# driver.execute_script('arguments[0].click()', botao_login)  # segunda forma de clicar, neste caso, é executado um comando javascript dentro do python

campo_email = driver.find_element(By.NAME, 'email')
campo_email.send_keys('machadodavid32@gmail.com')

campo_senha = driver.find_element(By.NAME, 'campoSenha')
campo_senha.send_keys('12345')

campo_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
campo_enviar.click()

input('')
driver.close()