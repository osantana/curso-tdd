from mocker import Mocker

mocker = Mocker()

response = mocker.mock()
response.read()
mocker.result("<html><head><title>test</title></head><body></body></html>")

urlopen = mocker.replace("urllib.urlopen")
urlopen("http://www.example.com")
mocker.result(response)

mocker.replay()

from urllib import urlopen
resp = urlopen("http://www.example.com")
content = resp.read()

from BeautifulSoup import BeautifulSoup
document = BeautifulSoup(content)
print document.html.head.title.string
