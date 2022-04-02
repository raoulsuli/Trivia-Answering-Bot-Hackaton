import nltk

def compute_freqs(text):
    words_res = nltk.word_tokenize(text)
    word_bigrams_res = list(nltk.bigrams(words_res))
    freqs = {}
    for item in word_bigrams_res:
        bigr = item[0] + ' ' + item[1]
        if bigr in freqs:
            freqs[bigr] += 1
        else:
            freqs[bigr] = 1
    return freqs


def who_is(text):
    frqs = compute_freqs(text)
    return frqs