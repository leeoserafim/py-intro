from requests import get
from bs4 import BeautifulSoup
from os import system, name
import re

system('cls') if (name == 'nt') else system('clear')

url='https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=user_rating,desc'

response=get(url)
#print(f'RESPONSE: {response.text}')

html_soup= BeautifulSoup(response.text, 'html.parser')

filmes= html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(f'Filmes listados: {len(filmes)}')

for i in range(len(filmes)):
    filmes_dados=filmes[i]
    nome=filmes_dados.h3.a.text
    lancamento=filmes_dados.h3.find('span', class_='lister-item-year text-muted unbold')
    votos= filmes_dados.find('span', attrs={'name':'nv'})
    episodio=filmes_dados.h3.find('small','text-primary unbold')
    x= ''
    if episodio is not None:
        ep = filmes_dados.find_all('a')
        x='-Episoio: ' + ep[2].text
    print('{} - {} {} \nPontuação: {} - Votos: {}\n'.format(i+1, nome,lancamento.text,filmes_dados.strong.text, votos.text))