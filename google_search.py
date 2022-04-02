import requests, re
from string import punctuation

def flatten(t):
    return [item for sublist in t for item in sublist]

def get_data():

    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "AIzaSyBhCgIZg7Dws2uciAPnh2F8J7KyMTShi8Q"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "e504c2a0af6824094"

    EXACT_TERMS = "lead singer"

    # the search query you want
    query = "Who is the lead singer of band Vita de Vie?"
    # using the first page
    page = 1
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?exactTerms={EXACT_TERMS}&key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    # make the API request
    data = requests.get(url).json()

    # get the result items
    search_items = data.get("items")

    # iterate over 10 results found
    output = []
    for i, search_item in enumerate(search_items, start=1):
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        text = f'{title} {snippet}'
        chars = f'{re.escape(punctuation)}”'
        output.append(re.sub(r'['+chars+']', '', text).split())
    return " ".join(flatten(output))

get_data()