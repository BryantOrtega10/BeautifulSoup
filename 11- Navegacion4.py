from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones I</h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1 "\
        "<ul class=\"submenu\"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')
print(soup.li.parent)
#<ul class="listaSimple listaInicial"><li>Item 1 <ul class="submenu"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>

print(soup.h1.string.parent)
#<h1>Investigación de Operaciones I</h1>

print(type(soup.html.parent))
#<class 'bs4.BeautifulSoup'>

print(soup.parent)
#None


print(soup.h1.parents)
#<generator object PageElement.parents at 0x00000277009C7A50>
for item in soup.h1.parents:
        print(item.name)
# body
# html
# [document]


