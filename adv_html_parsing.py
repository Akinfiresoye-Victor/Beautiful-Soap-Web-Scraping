'''This is useful because data might be embedded inside many tags so this can be used to get that data withouth mush complex code'''


from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')


bs=BeautifulSoup(html.read(), 'lxml')

#this will get the all the caracter written in green
namelist= bs.find_all('span',class_=[ 'green', 'red'])

#this wll get all the content on our webpage with the text 'the prince'
namelist= bs.find_all(text= 'the prince')

#this will get all the content with the class text and id of title
namelist= bs.find_all(id= 'title', class_='text')

print(len(namelist))
for name in namelist:
    print(name.get_text())
#This is the complex code i was talking about all this just to get a particular data and this isnt advisable
'''bs.find_all('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')'''
#in case like this you download the page or you use a mobile version of the site as it has cleaner html code
