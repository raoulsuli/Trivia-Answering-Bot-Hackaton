import sys, requests, os
from googlesearch import search
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

query = "Who is the president of the United States"

question_text = ""
question_type = ""
question_category = ""
answer_choices = []
answer_type = ""
idx = 0

def write_to_file(idx, text):
    if not os.path.exists("output"):
        os.mkdir("output")
    f = open(f"output/{idx}.txt", 'w')
    f.write(result)
    f.close()

for url in search(query, num = 10, stop = 10, pause = 2):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    result = soup.get_text()

    write_to_file(idx, result)

    idx += 1



nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
print(stop_words)
# total_words = query.split()
# total_word_length = len(total_words)
# print(total_word_length)
