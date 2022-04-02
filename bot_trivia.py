from bs4 import BeautifulSoup
import requests
import re
from textblob import TextBlob
import nltk


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "Who is the lead singer of band Vita de vie?"
urls = []
 
for j in search(query, tld="co.in", num=3, stop=3, pause=2):
    urls.append(j)


#lista care contine toate substantivele
nouns = []
r = requests.get(urls[0])
for word,pos in nltk.pos_tag(nltk.word_tokenize(str(query))):
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        nouns.append(word)

#lista de bigrame care contin substantive
words = nltk.word_tokenize(query)
tagged_words = nltk.pos_tag(words)
word_pairs = list(nltk.bigrams(tagged_words))
nouns_bi = []
for bigram in word_pairs:
	if bigram[0][1].startswith('N') or bigram[1][1].startswith('N'):
		nouns_bi.append(bigram)

final_bigrams = []
for item in nouns_bi:
	final_bigrams.append(item[0][0] + ' ' + item[1][0])
res_bigrams = []
for item in final_bigrams:
	res_bigrams.append(item.split())
print(res_bigrams)
