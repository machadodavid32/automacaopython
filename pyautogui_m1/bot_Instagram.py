import webbrowser, pyautogui
from time import sleep

while True:  # com isso meu codigo vai rodar todos os dias, infinitamente curtindo postagens nova da pagina escolhida

    # Acessando o site do instagram
    webbrowser.open_new_tab('https://instagram.com')
    sleep(1)
    # Entrar com o usuario

    pyautogui.click(877,358, duration=1)  # campo de usuario
    sleep(1)
    pyautogui.typewrite('David_Machado_dp')
    sleep(1)
    pyautogui.click(1100, 348, duration=1)
    sleep(1)
    pyautogui.click(891,407, duration=1)
    sleep(1)
    pyautogui.typewrite('*****')
    sleep(1)
    pyautogui.click(892,451, duration=1)
    sleep()
    # Clicar em login
    pyautogui.click(894,453, duration=1)
    sleep(1)

    # Pesquisar pela pagina
    pyautogui.click(697,640, duration=1)
    sleep(1)

    # clicar na buscar
    pyautogui.click(683,104, duration=1)
    sleep(1)
    # escrever na busca
    pyautogui.typewrite('devaprender')
    sleep(1)
    # clicar na pagina de destino
    pyautogui.click(620,224, duration=1)
    sleep(1)

    # Ir na postagem mais recente
    pyautogui.click(324,544, duration=1)
    sleep(2)


    #Verificar se já curtiu a pagina
    coracao = pyautogui.locateOnScreen('coracao.png')
    #Caso ja tenha curtido a pagina:
    if coracao is not None:
        sleep(86400)  # 86400 segundos = 24 horas
    elif coracao == None:
        pyautogui.click(876,842, duration=1)
        sleep(4)

    # Comentando
    pyautogui.click(943,946, duration=2)
    sleep(2)
    pyautogui.typewrite('comentario auto - Teste de automacao via Mestres da Auto')
    sleep(1)

    # Postando
    pyautogui.click(1286,952, duration=1)