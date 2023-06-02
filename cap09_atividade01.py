from requests import get
from bs4 import BeautifulSoup
from os import system, name
import re

system('cls') if (name == 'nt') else system('clear')

url='https://economia.uol.com.br'

response= get(url)
# print(f'Response: {str(response.text)}')

html_soup=BeautifulSoup(response.text, 'html.parser')
#print(f'\nHTML_SOUP: {html_soup}')

secao_dinheiro=html_soup.find_all('section', class_='currencies')
print(len(secao_dinheiro))
print(secao_dinheiro)

info= html_soup.find_all('div', class_='info')

info_valor=html_soup.find_all('span',class_='value bra')
print(info_valor)

relatorio=open('uol.txt', 'w', encoding='utf-8')
relatorio.write(html_soup.prettify())

valores=html_soup.find_all('a', class_='subtituloGrafico subtituloGraficoValor')
print(len(valores))
print(valores)

for valor in valores:
    v1=float(valor.text[-5:].replace(',','.'))
    print(v1)
    print(valor.text)
             