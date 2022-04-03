from urllib import response
import flask
from flask import jsonify, request
from frequencies import return_answer

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
    ret_ans = return_answer(question_contents.get('question_text'), choices, answer_type, "")
    ret_ans_formatted = ret_ans.title() if whoWhereType else ret_ans
    answer = jsonify({
        "answer": ret_ans_formatted
    })
    answer.status_code=200
    return answer

app.run(port=8000)