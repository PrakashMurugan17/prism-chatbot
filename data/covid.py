import urllib.request as ul
from bs4 import BeautifulSoup as soup
import regex as re



url = 'https://covid19.who.int/region/searo/country/in'
req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
client = ul.urlopen(req)
htmldata = client.read()
client.close()



pagesoup = soup(htmldata, "html.parser")
headings = pagesoup.findAll('span', {"class":"sc-fzoYHE dZCNaz"})
values = pagesoup.findAll('span', {"class":"sc-fznAgC jiWVsa"})





for a,b in headings, values:
    a = (re.sub('<[^>]*>', '', str(a)))
    b = (re.sub('<[^>]*>', '', str(b)))
    print(a +"\t"+ b)