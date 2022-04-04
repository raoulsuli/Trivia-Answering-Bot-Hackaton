import flask, nltk
from urllib import response
from flask import jsonify, request
from frequencies import return_answer

def extract_key_words(query):
	key_words = []
	for word,pos in nltk.pos_tag(nltk.word_tokenize(query)):
		if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
			key_words.append(word)
	return " ".join(key_words)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/sanity', methods=['GET'])
def check_sanity():
    response = jsonify({})
    response.status_code = 200
    return response

@app.route('/question', methods=['POST'])
def question():
    question_contents = request.get_json()
    question_text = question_contents.get('question_text')
    choices = [item.lower() for item in question_contents.get('answer_choices')]
    answer_type = question_contents.get('answer_type')
    firstQ = question_text.split()[0]
    whoWhereType = True if firstQ == 'Who' or firstQ == 'Where' else False
    ret_ans = return_answer(question_text, choices, answer_type, extract_key_words(question_text))
    ret_ans_formatted = ret_ans.title() if whoWhereType else ret_ans
    answer = jsonify({
        "answer": ret_ans_formatted
    })
    answer.status_code=200
    return answer

app.run(host="0.0.0.0", port=8000)