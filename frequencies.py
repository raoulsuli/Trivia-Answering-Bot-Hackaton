import nltk
from nltk.corpus import stopwords
from google_search import get_data
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


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
def who_is(text):
    frqs = compute_freqs(text)
    return frqs


def remove_words(text, stop_words_list):
	words = word_tokenize(text)
	result = []
	for word in words:
		if word not in stop_words_list:
			result.append(lemmatizer.lemmatize(word))
	return result

