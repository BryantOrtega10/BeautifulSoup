from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><head></head><body>"\
                    "<p>Investigación de Operaciones I</p></body></html>",
                    "html.parser")
print(soup)
print(soup.body.p)


