import sys, requests
from googlesearch import search
from bs4 import BeautifulSoup

query = sys.argv[1]

for url in search(query, num = 1, stop = 1, pause = 2):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())