"""
Estudo sobre web scraping com python.

Busca de gênero de bandas.
"""

# Importações
import requests
from bs4 import BeautifulSoup

# Entradas
banda = "Arctic Monkeys"

# Manipulação de Dados
banda = banda.replace(" ", "_")

# Raspagem da página HTML (estrutura de dados não aninhada)
wiki = "https://en.wikipedia.org/wiki/"
html = requests.get(wiki+banda)

# Criação do documento beautifulsoup (estrutura de dados aninhada)
soup = BeautifulSoup(html.content, 'html.parser')

# Procura por os termos chaves
genre = soup.find_all(class_='hlist hlist-separated')[0]
genre = genre.find_all('li')[0].get_text()

# Prints

print(genre)
