

from bs4 import BeautifulSoup
from urllib.request import urlopen


html= urlopen('http://www.pythonscraping.com/pages/page3.html')

bs=BeautifulSoup(html.read(), 'lxml')

#this will select the parent tag holding the src image location then goes on to the previous tag above the tag jolding the image and gets the content of that tag in text
print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())


