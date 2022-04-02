from googlesearch import search
import requests
from bs4 import BeautifulSoup
from string import punctuation
from nltk.corpus import stopwords

def flatten(t):
    return [item for sublist in t for item in sublist]

def get_data(query, terms):
    strings = []

    for url in search(query, num = 20, stop = 20, pause = 2):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        result = soup.find_all(['p', 'div', 'span'])

        for r in result:
            item = ''
            if (type(r.get_text()) == 'str'):
                item = r.get_text().get_text()
            else:
                item = r.get_text()
            if item != '' and item != '\n':
                strings.append(item.lower().split('\n'))

    arr = " ".join([item.translate(str.maketrans('', '', punctuation)) for item in flatten(strings) if item and item != ' '])
    
    stopwordsList = stopwords.words('english')
    termsQ = [item.lower() for item in query.split()]

    res = []

    for item in arr.split():
        if item not in list(termsQ) and item not in stopwordsList:
            res.append(item)

    return " ".join(res)