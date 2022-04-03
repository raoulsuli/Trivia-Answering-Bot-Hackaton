import nltk
from google_search import get_data
from word2number import w2n

def convert_num(num):
    try:
        return w2n.word_to_num(num)
    except Exception:
        return num

def has_numbers(inputString):
    return all(char.isdigit() for char in inputString)

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

def compute_freqs_one(text):
    textWithoutNumwords = " ".join([convert_num(item) for item in text.split()])
    newText = " ".join([item for item in textWithoutNumwords.split() if "'" not in item and has_numbers(item) == True])
    words_res = nltk.word_tokenize(newText)
    freqs = {}
    for item in words_res:
        bigr = item
        if bigr in freqs:
            freqs[bigr] += 1
        else:
            freqs[bigr] = 1

    return freqs

def return_answer(query, choices, answer_type, terms):
    data = get_data(query, terms)
    freqs = compute_freqs(data) if answer_type == 'text' else compute_freqs_one(data)
    if not choices:
        return max(freqs, key=freqs.get)
    else:
        sorted_dict = dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))
        for key in list(sorted_dict.keys()):
            if key in choices:
                return key
        return max(freqs, key=freqs.get)