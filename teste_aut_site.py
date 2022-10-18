import pyautogui
import webbrowser

# Abrir site
webbrowser.open('https://cursoautomacao.netlify.app/')  # Abrindo o site

pyautogui.moveTo(2241,779, duration=1) # indo com mouse pra pagina
pyautogui.scroll(-280) # descendo até o campo para escreve o nome
pyautogui.moveTo(2330,820)  # colocando o ponteiro no local exato para digitação
pyautogui.click()  # clicando para escrever o nome
pyautogui.typewrite('David')  # escrevendo o nome
pyautogui.click() # clicando em confirmar
pyautogui.moveTo(1977,171, duration=1) # Indo para a janela de ok
pyautogui.click() # Clicando na janela de ok
pyautogui.scroll(-1340) # descendo até a parte onde baixa os arquivos
pyautogui.moveTo(1410,174, duration=1) # link de download da planilha excel
pyautogui.click(button='left') # clicando para o download
pyautogui.moveTo(1579,171, duration=1) # link de donwload do arquivo pdf
pyautogui.click() # clicando para download
pyautogui.alert(text='VOCÊ TERMINOU', title='Confirmado!', button='ok')



# Obs: Na solução do professor, ele colocou sleep de 1 segundo entre as ações 

