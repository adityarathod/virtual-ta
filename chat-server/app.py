from flask import Flask, request
from flask_cors import CORS
from googlesearch import search
import requests


app = Flask(__name__)
CORS(app)


@app.route("/question")
def question():
    user = request.args.get('user')
    question = request.args.get('question')
    so_question = next(search('site:stackoverflow.com ' + question, stop=1))
    so_question_id = so_question.split("/")[4]
    api_call = f"https://api.stackexchange.com/2.3/questions/{so_question_id}/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody"
    response = requests.get(api_call).json()
    answer = response["items"][0]["body"]
    return f'The answer to {question} is {answer}'