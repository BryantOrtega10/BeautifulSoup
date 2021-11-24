from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><head></head><body>"\
                    "<b id=\"negrita\">Investigación de Operaciones I</b></body></html>",
                    "html.parser")
tag = soup.body.b
print(tag["id"])
#negrita
tag["id"] = "verybold"
tag["otro-atributo"] = 1
print(tag)
#<b id="verybold" otro-atributo="1">Investigación de Operaciones I</b>
del tag["id"]
print(tag)
#<b otro-atributo="1">Investigación de Operaciones I</b>
print(tag.attrs)
#{'otro-atributo': 1}

