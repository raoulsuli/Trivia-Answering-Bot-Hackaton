from urllib import response
import flask
from flask import jsonify, request
from frequencies_google import return_answer

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
    answer = jsonify({
        "answer": return_answer(question_contents.get('question_text'), "")
    })
    answer.status_code=200
    return answer

app.run('''host="0.0.0.0",'''port=8000)