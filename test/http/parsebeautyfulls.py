from bs4 import BeautifulSoup
import requests
import html5lib

url= "http://www.festo.com"
risp= requests.get(url)
dati= risp.text
print(dati)

beautyf=BeautifulSoup(dati,"html5lib")

for link in beautyf.find_all("a"):
    print(link.get("href"))

####parsing come parsek