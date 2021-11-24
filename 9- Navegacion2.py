from bs4 import BeautifulSoup

texto = "<html><head></head><body>"\
        "<h1>Investigación de Operaciones <span>I</span></h1>"\
        "<ul class=\"listaSimple listaInicial\"><li>Item 1</li><li>Item 2</li>"\
        "<li>Item 3</li><li>Item 4</li></ul>"\
        "<ul id=\"lista2\" class=\"listaSimple\"><li>Lista2 Item 1</li><li>Lista2 Item 2</li>"\
        "<li>Lista2 Item 3</li><li>Lista2 Item 4</li></ul>"\
        "</body></html>"

soup = BeautifulSoup(texto, 'html.parser')
print(soup.h1.contents)
#['Investigación de Operaciones ', <span>I</span>]
print(soup.ul.contents)
#[<li>Item 1</li>, <li>Item 2</li>, <li>Item 3</li>, <li>Item 4</li>]
print(soup.ul.children)
#<list_iterator object at 0x000001F5BF920CA0>
for hijo in soup.ul.children:
    print(hijo)


print(soup.h1.string.contents)
#AttributeError: 'NoneType' object has no attribute 'contents'

