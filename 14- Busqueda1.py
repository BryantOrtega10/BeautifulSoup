from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones I</h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1 "\
        "<ul class=\"submenu\"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')
print(soup.select("ul.submenu li:nth-of-type(2)"))
#[<li>SubMenu2</li>]
print(soup.select("#lista2"))
#[<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>Lista2 Item 2</li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>]







soup.find_all(string="Operaciones")
# ['Operaciones']

soup.find_all(string=["Operaciones", "SubMenu1", "SubMenu2"])
# ['Operaciones', 'SubMenu1', 'SubMenu2']

print(soup.find_all(id="lista2", limit=1))
#[<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>
# Lista2 Item 2</li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>]

print(soup.find(id="lista2"))
#<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>
# Lista2 Item 2</li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>

