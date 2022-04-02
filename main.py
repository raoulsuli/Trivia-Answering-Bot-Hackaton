import sys, requests, os
from googlesearch import search
from bs4 import BeautifulSoup

query = sys.argv[1]

idx = 0

def write_to_file(idx, text):
    if not os.path.exists("output"):
        os.mkdir("output")
    f = open(f"output/{idx}.txt", 'w')
    f.write(result)
    f.close()

for url in search(query, num = 10, stop = 10, pause = 2):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    result = soup.get_text()

    write_to_file(idx, result)

    idx += 1