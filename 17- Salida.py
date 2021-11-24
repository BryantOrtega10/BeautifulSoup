from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones I</h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1 "\
        "<ul class=\"submenu\"><li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')
print(soup)
#<html><head></head><body><h1>Investigación de Operaciones I</h1>
# <ul class="listaSimple listaInicial"><li>Item 1 <ul class="submenu">
# <li>SubMenu1</li><li>SubMenu2</li></ul></li><li>Item 2</li></ul>
# <ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>
# <li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul></body></html> 

print(soup.prettify())
print("\n")

# <html>
#  <head>
#  </head>
#  <body>
#   <h1>
#    Investigación de Operaciones I
#   </h1>
#   <ul class="listaSimple listaInicial">
#    <li>
#     Item 1
#     <ul class="submenu">
#      <li>
#       SubMenu1
#      </li>
#      <li>
#       SubMenu2
#      </li>
#     </ul>
#    </li>
#    <li>
#     Item 2
#    </li>
#   </ul>
#   <ul class="listaSimple" id="lista2">
#    <li>
#     Lista2 Item 1
#    </li>
#    <li>
#     Lista2 Item 2
#    </li>
#    <li>
#     Lista2 Item 3
#    </li>
#    <li>
#     Lista2 Item 4
#    </li>
#   </ul>
#  </body>
# </html>



print(soup.find(id="lista2"))
#<ul class="listaSimple" id="lista2"><li>Lista2 Item 1</li><li>Lista2 Item 2
# </li><li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>

print(soup.find(id="lista2").get_text())
#Lista2 Item 1Lista2 Item 2Lista2 Item 3Lista2 Item 4




markup = "<p\n>Paragraph 1</p>\n    <p>Paragraph 2</p>"
soup = BeautifulSoup(markup, 'html.parser')
for tag in soup.find_all('p'):
    print(repr((tag.sourceline, tag.sourcepos, tag.string)))
# (1, 0, 'Paragraph 1')
# (3, 4, 'Paragraph 2')



markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup, 'html.parser')
first_b, second_b = soup.find_all('b')
print(first_b == second_b)
# True

print(first_b.previous_element == second_b.previous_element)
# False




import copy
p_copy = copy.copy(soup.p)
print(p_copy)
# <p>I want <b>pizza</b> and more <b>pizza</b>!</p>
