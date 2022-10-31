from email.policy import default
from msilib.schema import Directory
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
# Acima estamos instanciando o webdriver usando o chrome

from webdriver_manager.chrome import ChromeDriverManager
# Acima facilita na hora da instalação pois o serviço webdriver_manager..
# ... trabalha com as atualizações do google chrome, sem a necessidade de ficar
# ... fazendo alterações a cada atualização

from selenium.webdriver.chrome.options import Options 

chrome_options = Options()
arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']
# Acima estamos configurando a inicialização da pagina, como por exemplo, a lingua, a resolução, o modo incognito,...etc..
# Abaixo, estão os argumentos mais comuns para inicialização
# start-maximized - inicia maximizado
# headless - roda em segundo plano
# disable-notifications - desabilita notificações
# disable-gpu - desabilita renderização na gpu
# window-size=  - importante definir a resolução, pois ai temos mais controle do tamanho da janela do site a ser trabalhado

for argument in arguments: # Para cada argumento dentro de arguments...
    chrome_options.add_argument(argument) # ..adicione em chrome_options

# Uso de configurações experimentais
chrome_options.add_experimental_option('prefs', {
    # alterar o local padrão de download de arquivos
    'download.default_directory': 'D:\\testes',
    # Notificar o google chrome sobre esta alteração
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
})


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options) # Adicionando as opções a 
# inicialização
# Acima estamos instalando o webdriver manager no chrome

# Navegar até o site usando o drive
driver.get('https://facebook.com')
input('Aperte uma tecla para fechar')

