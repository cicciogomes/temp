from html.parser import HTMLParser as hp
import urllib.request

risp=urllib.request.urlopen("http://www.festo.com")

pg= risp.read()
pg=str(pg)

class ClassPars(hp):
    def handle_starttag(self, tag: str, attrs) :
        if tag=="a":
            for name,value in attrs:
                if  name =="href":
                    print(value)
                
mPars = ClassPars()
mPars.feed(pg)

##restituisce link paagina