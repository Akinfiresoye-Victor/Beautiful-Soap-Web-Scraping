from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img', #getting all the image tags
#the \ backlash is used to treat a regex comand as part of the string it is used with / because it could cause some other errors in various languages
src=re.compile('\.\.\/img\/gifts/img.*\.jpg'))#this will take the values that start with that url and ends with jpg

for image in images:
    print(image['src'])
#../img/gifts/img3.jpg