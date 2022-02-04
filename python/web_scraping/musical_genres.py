"""
Estudo sobre web scraping com python.

Busca de gênero de bandas.

Reference: https://www.geeksforgeeks.org/web-scraping-from-wikipedia-using-python-a-complete-guide/
"""

# Importações
import requests
from bs4 import BeautifulSoup

# Entradas
banda = "Arctic Monkeys"

# Manipulação de Dados
banda = banda.replace(" ", "_")

# Raspagem da página HTML (estrutura de dados não aninhada)
wiki = "https://pt.wikipedia.org/wiki/"
html = requests.get(wiki+banda)

# Criação do documento beautifulsoup (estrutura de dados aninhada)
soup = BeautifulSoup(html.content, 'html.parser')

# Procura por os termos chaves
genre = soup.find("td", style="vertical-align: top; text-align: left;")
# print(genre)
