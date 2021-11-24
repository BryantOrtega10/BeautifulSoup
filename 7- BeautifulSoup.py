from bs4 import BeautifulSoup

doc = BeautifulSoup("<html><head></head><body>"\
                    "INSERTAR TITULO</body></html>",
                    "html.parser")
titulo = BeautifulSoup("<h1>Investigación de Operaciones I</h1>", "html.parser")
doc.find(text="INSERTAR TITULO").replace_with(titulo)
print(doc)
#<html><head></head><body><h1>Investigación de Operaciones I</h1></body></html>

