from gettext import find
import sys, requests, os, nltk
from googlesearch import search
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import shutil

query = "Who is the lead singer of band Vita de vie?"

question_text = ""
question_type = ""
question_category = ""
answer_choices = []
answer_type = ""
idx = 0
i = 0

NUM_PAGES = 10
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

shutil.rmtree("output", ignore_errors=True)
os.mkdir("output")

#lista bigrame care contin substantive
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
# print(final_bigrams)
#print(soup.prettify())
print(final_bigrams)

answer_docs = []

for url in search(query, num = 30, stop = 30, pause = 2):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(url)
    result = soup.find_all('p')

    f = open(f"output/{idx}.txt", 'a')

    for rr in result:
        answer_docs.append(rr.get_text())
        f.write(rr.get_text())

    f.close()
    
    idx += 1


words = nltk.word_tokenize(query)
tagged_words = nltk.pos_tag(words)
word_pairs = list(nltk.bigrams(tagged_words))
nouns_bi = []
for bigram in word_pairs:
    if (bigram[0][1].startswith('N') and bigram[1][1].startswith('J')) or (bigram[0][1].startswith('J') and bigram[1][1].startswith('N')):
	#if bigram[0][1].startswith('N') or bigram[1][1].startswith('N'):
	    nouns_bi.append(bigram)

final_bigrams = []
for item in nouns_bi:
	final_bigrams.append(item[0][0] + ' ' + item[1][0])
res_bigrams = []
for item in final_bigrams:
	res_bigrams.append(item.split())

info = []
result = []

for doc in answer_docs:
    sentences = sent_tokenize(doc)
    for sentence in sentences:
        for bigram in res_bigrams:
            if sentence.find(bigram[0]) != -1 and sentence.find(bigram[1]) != -1:
                result.append(sentence)
all_sentences = list(set(result))


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


def who_is():
    text = " ".join(all_sentences)
    frqs = compute_freqs(text)
    return frqs

    idx += 1

cwd = os.getcwd()
words_bigrams = []
for bigram in final_bigrams:
    words_bigrams.append(bigram.split())
# print(words_bigrams)
for filename in os.listdir("output/"):
    with open(cwd + "/output/" + filename, 'r') as f:
        text = f.read()
    temp = [i.strip() for i in text.split('.')]
    for propozitie in temp:
        if (propozitie.find(words_bigrams[0][0]) != -1 and propozitie.find(words_bigrams[0][1]) != -1):
            print(propozitie)
# with open(cwd + "/output/" + "0.txt", 'r') as f:
    # text = f.read()
    # temp = [i.strip() for i in text.split('.')]
    # for propozitie in temp:
    #     if (propozitie.find(words_bigrams[0][0]) != -1 and propozitie.find(words_bigrams[0][1]) != -1):
    #         print(propozitie)
    idx += 1
print(who_is())
 
