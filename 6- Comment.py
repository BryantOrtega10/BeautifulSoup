from bs4 import BeautifulSoup

texto = "<b><!--Comentario que en formato html--></b>"
soup = BeautifulSoup(texto, 'html.parser')
comment = soup.b.string
print(type(comment))
#<class 'bs4.element.Comment'>

print(comment)
#Comentario que en formato html


print(soup.prettify())
# <b>
#  <!--Comentario que en formato html-->
# </b>

