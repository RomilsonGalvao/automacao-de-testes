import requests
from bs4 import BeautifulSoup
noticia = requests.get('https://g1.globo.com')
content = noticia.content
site = BeautifulSoup(content, 'html.parser')
postagem = site.find('div', attrs={'class': 'feed-post-body-title gui-color-primary gui-color-hover'})
print(postagem.text)