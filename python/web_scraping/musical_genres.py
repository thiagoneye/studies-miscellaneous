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
wiki = "https://pt.wikipedia.org/wiki/"
html = requests.get(wiki+banda)

# Criação do documento beautifulsoup (estrutura de dados aninhada)
soup = BeautifulSoup(html.content, 'html.parser')

# Procura por os termos chaves
genre = soup.find(class_='mw-workspace-container')
genre = genre.find(class_='mw-content-container')
genre = genre.find(id='content')
genre = genre.find(id='bodyContent')
genre = genre.find(id='mw-content-text')
genre = genre.find_all(class_='infobox infobox infobox_v2')[0]
genre = genre.find_all('tr')[5].find_all('a')[1].get_text()

# Prints

print(genre)
