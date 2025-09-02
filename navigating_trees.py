'''Navigating trees ae a way of mapping out all tags and subtags so we can have a clear overview of what data we want to get '''

from bs4 import BeautifulSoup
from urllib.request import urlopen


html= urlopen('http://www.pythonscraping.com/pages/page3.html')

bs=BeautifulSoup(html.read(), 'lxml')


''' the html page is mapped out like this 
HTML
— body
— div.wrapper
— h1
— div.content
— table#giftList
— tr
— th
— th
— th
— th
— tr.gift#gift1
— td
— td
— span.excitingNote
— td
— td
— img
— ...table rows continue...
— div.footer
'''

#this will get all the children tags of the parent tag the parent tag is the tag next to <table> then the next tag under that is the child and it grabs all the contentand tags inside that
#while the .descendat will get all the child and grndchild content
for child in bs.find('table', id= 'giftList').children:
    print(child)

