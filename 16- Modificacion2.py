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
tag.string = "Investigación de Operaciones I - Grupo 020-82"
tagUl = soup.find(id="lista2")
tagLi = soup.new_tag("li")
tagLi.string = "Lista2 Item 5"
tagUl.append(tagLi)
print(tag)
#<h1>Investigación de Operaciones I - Grupo 020-82</h1>
print(tagUl)
#<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>
#<li>Lista2 Item 3</li><li>Lista2 Item 4</li><li>Lista2 Item 5</li></ul>

tagUl.clear()
print(tagUl)
#<ul class="listaSimple" id="lista2"></ul>
tagOl = soup.new_tag("ol")
tagOl.append(tagLi)
tagUl.replace_with(tagOl)
print(soup)
#<html><head></head><body><h1>Investigación de Operaciones I - Grupo 020-82</h1>
# <ul class="listaSimple listaInicial"><li>Item 1 <ul class="submenu"><li>SubMenu1</li>
# <li>SubMenu2</li></ul></li><li>Item 2</li></ul><ol><li>Lista2 Item 5</li>
# </ol></body></html>




soup = BeautifulSoup("<b>dejar</b>", 'html.parser')
tag = soup.new_tag("i")
tag.string = "NO"
soup.b.string.insert_after(tag)
soup.b
# <b>dejar<i>NO</i></b>




soup = BeautifulSoup("<p>I wish I was bold.</p>", 'html.parser')
soup.p.string.wrap(soup.new_tag("b"))
# <b>I wish I was bold.</b>

soup.p.wrap(soup.new_tag("div"))
# <div><p><b>I wish I was bold.</b></p></div>



markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

a_tag.i.unwrap()
a_tag
# <a href="http://example.com/">I linked to example.com</a>