
import requests
from bs4 import BeautifulSoup
import random
import re
import time
from fake_useragent import UserAgent


ue=UserAgent().random
#function that opens and crawl into a  url
def getLinks(articleUrl):
    #setting our url we want to open
    url = f"https://en.wikipedia.org{articleUrl}"
    #creating our header so we can bypass the browser restrictions
    headers = {"User-Agent": ue}
    #gets the content inside the url
    r = requests.get(url, headers=headers)
    r.raise_for_status()  # crash cleanly if request fails
    bs = BeautifulSoup(r.text, "html.parser")
    #returns all the link that leads to an article from the first content section it can find
    return bs.find("div", id="bodyContent").find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))

#we are starting with this link 
links = getLinks("/wiki/Kevin_Bacon")

#were puting the sites we have visited into a set because its easier to acess and manage
visited = set()
for _ in range(20):  # limit to 20 steps
    #if we got an empty link we break so we dont get an error
    if not links:
        break
    #gets a random link from te list of links we extracted from the content
    newArticle = random.choice(links).attrs["href"]
    #if we have visited the link before we skip to get another
    if newArticle in visited:
        continue
    #add links weve visited so wwe wont have to revisit it 
    visited.add(newArticle)
    #print each of the link to articles we are receiving
    print(newArticle)
    #we the dive deeper in that link weve gotten 
    links = getLinks(newArticle)
    time.sleep(1)  # be polite cos if you spam wikipedia with hundrends of request per second theyll block your IP
