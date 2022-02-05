import http.client

connessione = http.client.HTTPConnection("www.httpbin.org")
connessione.request("GET","/form/post")
rispostaServer= connessione.getresponse()

print(rispostaServer.status,rispostaServer.reason)