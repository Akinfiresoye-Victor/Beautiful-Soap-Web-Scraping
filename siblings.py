

from bs4 import BeautifulSoup
from urllib.request import urlopen


html= urlopen('http://www.pythonscraping.com/pages/page3.html')

bs=BeautifulSoup(html.read(), 'lxml')

#this will skip the first title row(tr) then go to the next tag
for sibling in bs.find('table', id= 'giftList').tr:
    print(sibling)

