from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
# Acima estamos instanciando o webdriver usando o chrome

from webdriver_manager.chrome import ChromeDriverManager
# Acima facilita na hora da instalação pois o serviço webdriver_manager..
# ... trabalha com as atualizações do google chrome, sem a necessidade de ficar
# ... fazendo alterações a cada atualização

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Acima estamos instalando o webdriver manager no chrome

# Navegar até o site usando o drive

driver.get('https://facebook.com')
input('Aperte uma tecla para fechar')

