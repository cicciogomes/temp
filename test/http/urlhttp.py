import urllib.request
import urllib.error
try:
    url="http://www.festo.com"
    risp=urllib.request.urlopen(url)
    print(risp.code)
    if risp.code==200:
        print(risp.headers)
except urllib.request.URLError as errore:
    print(errore.reason)

except urllib.error.HTTPError as errore2:
    print(errore2.reason)