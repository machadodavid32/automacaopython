"""
Aqui estamos pesquisando via seletores css na pagina usando a mesma forma de pesquisa, com f12 e depois ctrl f
e dai coloca o nome da classe, como por exemplo:
.btn btn-success - > Aqui são dois elementos em uma classe, o elemento btn e o elemento btn-success

Outro exemplo é pelo ID, da seguinte forma:

#maisonomedoid

ex: #dropdownMenuButton

Desta forma, temos as seguintes situações para pesquisas:

tag (section, div, h4, button)
class (.btn)
Combinação de class (.btn .btn-success)
id (#dropdownMenuButton)

Essas acima são as formas mais genéricas de pesquisa. Temos outras formas mais sofisticadas:

tag[atributo='valor']

Exemplo:
input[class='form-check-input']

input[class^='form'] - aqui vai mostrar todos os inputs com a que começam com form

input[class$='input'] - vai mostrar todos os elementos que terminam com 'input'

input[class*='check'] - vai mostrar todos os elementos pelo valor, ou seja, todos os elementos chamados 'check' dentro da classe input

E como poderíamos utilizar isso no python?

Desta forma (exemplos):

elemento_h2 = driver.find_element(By.CSS_SELECTOR, 'h2')

elemento_check = driver.find_element(By.CSS_SELECTOR, 'input[class*="check"]')

elemento_ipunt = driver.find_element(By.CSS_SELECTOR, 'input[class$="input"]')

OBS: posso usat tanto o xpath quanto o css selector para fazer minhas automações


"""