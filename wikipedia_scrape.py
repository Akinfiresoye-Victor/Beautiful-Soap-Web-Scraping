from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#library used to generate headers
from fake_useragent import UserAgent
import re
import datetime

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

#this then will give us a random header which will be used to bypass wikipedia restrictions against web crawlers
ua = UserAgent().random

#the header must be in a dictionary at all times
headers = {"User-Agent": ua}

#hie header is then used as disguise with the url to retrieve data from the webpage
req = Request(url, headers=headers)


#we can now have access to the webpage
html = urlopen(req)
# The rest of your scraping code goes here


# bs = BeautifulSoup(html, 'html.parser')

# #looping through to get the content in our a tag
# for link in bs.find_all('a'):
#     #then we check for the href attribute in the a tag
#     if 'href' in link.attrs:
#         #then prints the contents inside
#         print(link.attrs['href'])

bs = BeautifulSoup(html, 'html.parser')
#a way to get the link containg the link to articles because they follow a particular pattern
#the pattern is saying that the link must beging with /wiki/ and must not contain a column 
articles= bs.find('div', id='bodyContent').find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
for link in articles:
    if 'href' in link.attrs:
        print(link.attrs['href'])