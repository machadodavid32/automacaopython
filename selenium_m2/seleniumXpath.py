
"""
xpath
sintaxe -> //tag[@atributo='valor']

Na pagina de um navegador, apertar F12 e apertar crtl F pra digitar o xpath

alguns exemplos:
//*[h4] - procura todos os h4 dentro da pagina.

//*[contains(text(), 'exemplo')] - procura todos os textos com a palavra exemplo
Qualquer tag que contenha a propriedade texto com a palavra 'exemplo'

Outro exemplo: //*[contains(text(), 'exemplo')] or //*[contains(text(), 'paragrafo')]
Neste caso vai achar mais outra palavras

Além de 'or', podemos utilizar no meio ali a palavra end

//*[starts-with(text(), 'Exemplo')] - Este vai achar todas as palavras que começam por 'Exemplo'

//*[starts-with(@class, 'btn')] - Retorna todos os elementos que possuem a classe inicial de btn

//h4[text()='Exemplo checkbox'] - é a melhor forma de organizar sua automação, utilizar a tag no lugar do *

//section[@class='jumbotron'] - procurando por uma class chamada jumbotron


//div[@id='select-class-example']//fieldset/h4 -> Aqui, estamos pesquisando por elemento dentro de um elemento...
..aqui é o elemento chamado 'select-class-example', que está dentro da tag h4, qu está dentro da tag fieldset, que está dentro...
.. da tag div. Antes do h4, temos apenas uma barra /, neste caso significa que queremos o proximo filho logo abaixo da tag...
... e caso tenhamos mais de um filho, usar // e específicar a tag correta com o indice correto. Conforme exemplo abaixo:

//thead//tr//th[3]

E após conseguir o xpath correto, vc usa da seguinte forma no python
Exemplo:
driver.find_element(By.XPATH,"//thead//tr//th[3]")
   

"""