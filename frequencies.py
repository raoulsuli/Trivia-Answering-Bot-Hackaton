import nltk
from google_search import get_data

def compute_freqs(text):
    newText = " ".join([item for item in text.split() if "'" not in item])
    words_res = nltk.word_tokenize(newText)
    word_bigrams_res = list(nltk.bigrams(words_res))
    freqs = {}
    for item in word_bigrams_res:
        bigr = item[0] + ' ' + item[1]
        if bigr in freqs:
            freqs[bigr] += 1
        else:
            freqs[bigr] = 1
    return freqs

query = "What's the name of Simba's nasty uncle in Lion King?"
terms = "Simba"

data = get_data(query, terms)
freqs = compute_freqs(data)

print(dict(sorted(freqs.items(), key=lambda item: item[1])))