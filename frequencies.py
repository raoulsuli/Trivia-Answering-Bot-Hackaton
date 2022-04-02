import nltk
from google_search import get_data

def compute_freqs(text):
    words_res = nltk.word_tokenize(text)
    word_bigrams_res = list(nltk.bigrams(words_res))
    freqs = {}
    for item in word_bigrams_res:
        bigr = (item[0] + ' ' + item[1]).lower()
        if bigr in freqs:
            freqs[bigr] += 1
        else:
            freqs[bigr] = 1
    return freqs

data = get_data(query = "Who is the lead singer of band Vita de vie?", terms = "lead singer")
freqs = compute_freqs(data)

print(dict(sorted(freqs.items(), key=lambda item: item[1])))