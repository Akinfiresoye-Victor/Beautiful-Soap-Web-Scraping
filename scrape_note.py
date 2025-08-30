# In web Scraping a lot of error can be found so we have to handle all this error using try and except blocks

#urlopen('url')  this is used to make a particular url accesscible to our code to allow us to get the requiered information for it

#if the link is assigned with a variable-html it can get all the html code onto our terminal using html.read()
#BeautifulSoup(html.read(), 'external_help') BS can now be used to get specific data with ext help like lxml,html.parser, html5lib to help format our data that is going to be extracted

#if bs was the variable holding 👆 we can get the result of what we scraped by 👇 it would get all the values that has the h1 tag which is usually the title
'''
bs.body.html
bs.h1
bs.html.h1
bs.html.body.h1
'''

# HTTPError and URLError are 2 main error that deals with httprequests
#URLError pops up when the url opened isnt found, while HTTPError just arises if the server returned a bad request