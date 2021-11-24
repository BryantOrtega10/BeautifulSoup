from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones I</h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1 "\
        "<ul class=\"submenu\"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')
tag = soup.h1
tag.name = "h2"
tag["class"] = "titulo"
tag["id"] = "titulo1"
print(tag)

del tag['class']
print(tag)




markup = '<a href="http://ejemplo.com/">Este es un link a <i>ejemplo.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')

tag = soup.a
tag.string = "Nuevo texto."
tag
# <a href="http://ejemplo.com/">Nuevo texto.</a>


