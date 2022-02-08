"""
Estudo sobre web scraping com python.

Busca de gênero de bandas.
"""

# Importações
import requests
from bs4 import BeautifulSoup

# Entradas
banda = "5 Seconds of Summer"

# Manipulação de Dados
banda = banda.replace(" ", "_")

# Raspagem da página HTML (estrutura de dados não aninhada)
wiki = "https://pt.wikipedia.org/wiki/"
html = requests.get(wiki+banda)

# Criação do documento beautifulsoup (estrutura de dados aninhada)
soup = BeautifulSoup(html.content, 'html.parser')

# Procura por os termos chaves
try:
    genre = soup.find_all(class_='infobox infobox infobox_v2')[0]
    genre = genre.find_all('tr')

    for i in range(len(genre)):
        try:
            value = genre[i].find(scope='row').get_text()[:9]
            if value == 'Gênero(s)':
                genre = genre[i].find_all('a')[1].get_text()
                get_value = True
        except:
            value = "It's not that"
except:
    get_value = False

if not get_value:
    genre = soup.find_all(class_='infobox infobox_v2')[0]
    genre = genre.find_all('tr')

    for i in range(len(genre)):
        try:
            value = genre[i].find(scope='row').get_text()[:9]
            if value == 'Gênero(s)':
                genre = genre[i].find_all('a')[1].get_text()
                get_value = True
        except:
            value = "It's not that"

print(genre)
