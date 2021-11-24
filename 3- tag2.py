from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><head></head><body>"\
                    "<b id=\"negrita\" class=\"negrita titulo\">Investigación de Operaciones I</b></body></html>",
                    "html.parser")
tag = soup.body.b
print(tag.attrs)
#{'id': 'negrita', 'class': ['negrita', 'titulo']}







#print(tag["id"])
#tag["id"] = "verybold"
#tag["otro-atributo"] = 1
#print(tag)

