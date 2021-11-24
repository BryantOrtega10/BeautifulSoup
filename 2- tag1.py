from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><head></head><body>"\
                    "<p>Investigación de Operaciones I</p></body></html>",
                    "html.parser")
print(soup.body.p.name)

type(soup.body.p)
#p
soup.body.p.name = "h1"
type(soup.body.h1)
#h1

print(soup.body)

