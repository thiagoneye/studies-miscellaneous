"""
Estudo sobre web scraping com python.

Busca de temperaturas mínimas e máximas.
Referência: https://blog.geekhunter.com.br/como-fazer-um-web-scraping-python/

Requests é uma biblioteca HTTP para a linguagem de programação Python. O
objetivo do projeto é tornar as solicitações HTTP mais simples e mais amigáveis.

Beautiful Soup é um pacote Python para análise de documentos HTML e XML. Ele
cria uma árvore de análise para páginas analisadas que podem ser usadas para
extrair dados de HTML, o que é útil para web scraping.
"""

# Importações
import requests
from bs4 import BeautifulSoup

# Raspagem da página HTML (estrutura de dados não aninhada)
html = requests.get("https://www.climatempo.com.br/")

# Criação do documento beautifulsoup (estrutura de dados aninhada)
soup = BeautifulSoup(html.content, 'html.parser')

# Visualização do documento beautifulsoup
# print(soup.prettify())

# Procura por os termos chaves
#temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
temperatura = soup.find("p", class_="-gray _flex _align-center")
t_min = int(temperatura.contents[2][1:3])
t_max = int(temperatura.contents[2*2][1:3])

print("Hoje, em São Paulo, a temperatura mínima é de " + str(t_min) + "°.")
print("Hoje, em São Paulo, a temperatura máxima é de " + str(t_max) + "°.")
