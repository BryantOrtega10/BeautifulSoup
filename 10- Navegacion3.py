from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones I</h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1 "\
        "<ul class=\"submenu\"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')

for hijo in soup.ul.children:
    print(hijo)
# <li>Item 1 <ul class="submenu"><li>SubMenu1</li><li>SubMenu2</li></ul></li>
# <li>Item 2</li>

print("\n")

for des_recursivo in soup.ul.descendants:
    print(des_recursivo)
# <li>Item 1 <ul class="submenu"><li>SubMenu1</li><li>SubMenu2</li></ul></li>
# Item 1
# <ul class="submenu"><li>SubMenu1</li><li>SubMenu2</li></ul>
# <li>SubMenu1</li>
# SubMenu1
# <li>SubMenu2</li>
# SubMenu2
# <li>Item 2</li>
# Item 2




