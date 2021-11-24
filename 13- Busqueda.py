from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h2>Investigación de Operaciones I</h2><h2>Pruebas</h2>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1 "\
        "<ul class=\"submenu\"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')


print(soup.find_all("h2"))
#[<h2>Investigación de Operaciones I</h2>, <h2>Pruebas</h2>]

print(soup.find_all("ul","submenu"))
#[<ul class="submenu"><li>SubMenu1</li><li>SubMenu2</li></ul>]

print(soup.find_all(class_="listaSimple"))
#[<ul class="listaSimple listaInicial"><li>Item 1 <ul class="submenu"><li>SubMenu1</li>
# <li>SubMenu2</li></ul></li><li>Item 2</li></ul>, <ul class="listaSimple" id="lista2">
# <li>Lista2 Item 1</li><li>Lista2 Item 2</li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>]

print(soup.find_all(string="SubMenu2"))
#['SubMenu2']

print(soup.find_all(id="lista2"))
#[<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>Lista2 Item 2</li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>]


print(soup.find_all(id=True, class_="listaSimple"))
#[<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>Lista2 Item 2</li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>]



data_soup = BeautifulSoup('<div data-cualquier="value">Cualquier cosa!</div>', 'html.parser')
data_soup.find_all(attrs={"data-cualquier": "value"})
# [<div data-cualquier="value">Cualquier cosa!</div>]


name_soup = BeautifulSoup('<input name="email"/>', 'html.parser')
name_soup.find_all(name="email")
# []
name_soup.find_all(attrs={"name": "email"})
# [<input name="email"/>]




