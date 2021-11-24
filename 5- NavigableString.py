from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><head></head><body>"\
                    "<b id=\"negrita\">Investigación de Operaciones I</b></body></html>",
                    "html.parser")
tag = soup.body.b
print(tag.string.contents)



print(type(tag.string))

#<class 'bs4.element.NavigableString'>

tag.string.replace_with("Otro texto")
print(tag)
#<b id="negrita">Otro texto</b>
