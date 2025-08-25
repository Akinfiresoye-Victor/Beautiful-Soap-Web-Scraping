#importing a function that opens a link giving us access to thin information in that link
from urllib.request import urlopen

#we assign the opened link to the variable html
html=urlopen("http://pythonscraping.com/pages/page1.html")

#this reads the information stored in the link
print(html.read())

