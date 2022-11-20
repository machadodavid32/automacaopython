from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()


# Entrar no site do instagram
driver.get('https://www.instagram.com/')

# Clicar e digitar meu usuário
campo_usuario = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, 
"//input[@name='username']")))
campo_usuario.send_keys("david_machado_dp")
sleep(3)

# Clicar e digitar minha senha 
campo_senha = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH,
 "//input[@name='password']")))
campo_senha.send_keys('#Ns8493ni')
sleep(3)

# Clicar no campo entrar
botao_entrar = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, 
"//div[text()='Entrar']")))
botao_entrar.click()
sleep(2)

# Segunda tela de loguin
campo_informacao_login = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH,
 "//*[text()='Agora não']")))
sleep(2)
campo_informacao_login.click()
sleep(2)

# Pesquisar a pagina
#campo_pesquisa = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH,
# "//*[text()='Pesquisa']")))
#campo_pesquisa[0].click
#sleep(1)
#campo_pesquisa.send_keys('devaprender')

# Navegar até a página alvo
while True:  # Para rodar o codigo de forma infinita
    driver.get('https://www.instagram.com/devaprender/')
    sleep(2)

    # Clicar na última  postagem
    postagens = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH, 
    "//div[@class='_aagw']")))  # Pois foram encontrados multiplos elementos, ...
    # e como queremos o primeiro, deve funcionar.
    sleep(2)
    postagens[0].click()
    sleep(2)

    elementos_postagem = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH,
    "//div[@class='_abm0 _abl_']")))

    if len(elementos_postagem) == 4:
        elementos_postagem[0].click()
    else:
        print("Postagem já foi curtida")
        sleep(86400)  # Aqui é a pausa de 24 horas


#  Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
input('')
driver.close()