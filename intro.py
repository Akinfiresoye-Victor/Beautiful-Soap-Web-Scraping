'''Basic web scraper code with BeautifulSoup'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# opening the link to read
html=urlopen("http://pythonscraping.com/pages/page1.html")
#using beautiful soup to get specific data, even withouth the .read we will get a more precise data
bs= BeautifulSoup(html, 'html.parser')
# lxml is better than html.parser bcos it fixes messy html code and is better in parsing messy html code it's faster in general
bs= BeautifulSoup(html.read(), 'lxml')#lxml must be used with a .read() function

#it is slower than both but good when working with messy or handwritten html sites
bs =BeautifulSoup(html.read(), 'html5lib')
#this will return the first line of code that has the h1 tag
#if no data is found it will return none
'''All this will return the same output'''
print(bs.h1)
print(bs.body.h1)
print(bs.html.body.h1)
print(bs.html.h1)

