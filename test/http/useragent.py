from urllib.request import Request
from urllib.request import urlopen

rich = Request("http://www.festo.com")

urlopen(rich)

print(rich.get_header("User-agent"))
