"""
Estudo sobre web scraping com python.

Trecho de Alice no País das Maravilhas.
Referência: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
"""

# Importação
from bs4 import BeautifulSoup

# Entradas
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Documento beautifulsoup
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())

alice_title = soup.title.string
print(alice_title)
print(alice_title[0])
