import nltk
from nltk.corpus import stopwords
from google_search import get_data
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


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


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

data = get_data(query="Which ocean is Bermuda in?", terms="ocean Bermuda")
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

