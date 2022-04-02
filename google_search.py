import requests, re
from string import punctuation
from nltk.corpus import stopwords

def flatten(t):
    return [item for sublist in t for item in sublist]

def get_data(query, terms):

    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "AIzaSyDUB5AoQ9HclzvVz9khCYy9m4brjAkWlLM"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "e504c2a0af6824094"

    # using the first page
    page = 1
    
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?exactTerms={terms}&key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    # make the API request
    data = requests.get(url).json()

    # get the result items
    search_items = data.get("items")

    # iterate over 10 results found
    output = []
    for i, search_item in enumerate(search_items, start=1):
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        text = f'{title} {snippet}'.lower()
        chars = f'{re.escape(punctuation)}”'.replace("'", "")
        output.append(re.sub(r'['+chars+']', '', text).split())

    stopwordsList = stopwords.words('english')
    terms = [item.lower() for item in query.split()]

    res = []

    for item in flatten(output):
        if item not in list(terms) and item not in stopwordsList:
            res.append(item)

    return " ".join(res)
