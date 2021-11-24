from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones I</h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1</li><li>Item 2</li>"\
        "<li>Item 3</li><li>Item 4</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')
print(soup.h1)
#<h1>Investigación de Operaciones I</h1>
print(soup.ul)
#<ul class="listaSimple listaInicial"><li>Item 1</li><li>Item 2</li><li>Item 3</li><li>Item 4</li></ul>


print(soup.body.h1)
#<h1>Investigación de Operaciones I</h1>

