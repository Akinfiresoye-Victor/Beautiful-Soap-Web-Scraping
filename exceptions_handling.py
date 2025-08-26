'''Most webpages has messy/poorly formatted data, so to avoid scraping error while the crawler is activewe use thiis means
to handle error withouth breaking your code or data being scrapped'''

from urllib.request import urlopen
#error handlers when dealing with requests or interraction with the web page
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

#try block to check or handle all the errors going to be passes through
try:
    html= urlopen('http://pythonscraping.com/pages/page1.html')
#This will pop up when the url wasnt retrieve the sata from the site successfully
except HTTPError as e:
    print(e)
#This will pop up when the url we open isnt found
except URLError as e:
    print(f'The server Could not be found!')
#Then if the url was successfuly opened it would print 👇
else:
    print('It Worked')
    

bs= BeautifulSoup(html.read(), 'lxml')

#A way of handling errors if a particular tag wasnt find while looking for one
try:
#this will return either a tag object(True) or None(False)
    badContent = bs.find("nonExistingTag")
#if none was found it returns The error
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print ('Tag was not found')
    else:
        print(badContent)
        
# Function to get the title from a webpage
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs= BeautifulSoup(html.read(), 'html.parser')
        title= bs.body.h1
#this will if wat we are trying to do cant be done on this type of object incase bs returns none we cant read a none value
    except AttributeError as e:
        return None
    #if all check is pass we get the title
    return title

#we then run the function by passing this url to the function
result=getTitle('http://www.pythonscraping.com/pages/page1.html')
if result == None:
    print('Title Could not be found')
else:
    print(result)
