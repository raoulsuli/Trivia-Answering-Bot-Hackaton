import nltk
from google_search import get_data

def compute_freqs(text):
    newText = " ".join([item for item in text.split() if "'" not in item])
    words_res = nltk.word_tokenize(newText)
    word_bigrams_res = list(nltk.bigrams(words_res))
    freqs = {}
    for item in word_bigrams_res:
        bigr = item[0] + ' ' + item[1]
        revBigr = item[1] + ' ' + item[0]
        if bigr in freqs:
            freqs[bigr] += 1
        elif revBigr in freqs:
            freqs[revBigr] += 1
        else:
            freqs[bigr] = 1

    return freqs

def return_answer(query, terms):
    data = get_data(query, terms)
    freqs = compute_freqs(data)
    return max(freqs, key=freqs.get)

