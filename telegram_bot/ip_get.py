from urllib.request import urlopen
from bs4 import BeautifulSoup
import geocoder

html = urlopen('https://pr-cy.ru/browser-details/')
bs = BeautifulSoup(html.read(), 'html.parser')
ip = bs.find('div', {'class':'ip'}) 
my = ip.get_text()
g = geocoder.ip(my)
print(g.latlng)

