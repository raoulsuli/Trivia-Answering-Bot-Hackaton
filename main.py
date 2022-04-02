import sys, requests, os, nltk
from googlesearch import search
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

query = "Who is the lead singer of band Vita de vie?"

question_text = ""
question_type = ""
question_category = ""
answer_choices = []
answer_type = ""
idx = 0

<<<<<<< Updated upstream
NUM_PAGES = 10

for url in search(query, num = NUM_PAGES, stop = NUM_PAGES, pause = 2):
=======
#lista bigrame care contin substantive
words = nltk.word_tokenize(query)
tagged_words = nltk.pos_tag(words)
word_pairs = list(nltk.bigrams(tagged_words))
nouns_bi = []
for bigram in word_pairs:
	if bigram[0][1].startswith('N') or bigram[1][1].startswith('N'):
		nouns_bi.append(bigram)

#soup = BeautifulSoup(r.content, 'html5lib')
#print(nouns_bi)
final_bigrams = []
for item in nouns_bi:
	final_bigrams.append(item[0][0] + ' ' + item[1][0])
print(final_bigrams)
#print(soup.prettify())

for url in search(query, num = 1, stop = 1, pause = 2):
>>>>>>> Stashed changes
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    result = soup.find_all('p')
    
    if not os.path.exists("output"):
        os.mkdir("output")

    os.remove(f"output/{idx}.txt")

    f = open(f"output/{idx}.txt", 'a')

    for rr in result:
        f.write(rr.get_text())

    f.close()

    idx += 1

find(final_bigrams)