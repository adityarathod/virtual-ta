from flask import Flask, request
from flask_cors import CORS
from googlesearch import search
import requests
import json


app = Flask(__name__)
CORS(app)


def google(question):
    so_question = next(search('site:stackoverflow.com ' + question, stop=1))
    so_question_id = so_question.split("/")[4]
    api_call = f"https://api.stackexchange.com/2.3/questions/{so_question_id}/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody"
    response = requests.get(api_call).json()
    answer = response["items"][0]["body"]
    return f'The answer to {question} is {answer}'


def rasa(user, question):
    url = "http://localhost:5005/webhooks/rest/webhook"

    payload = json.dumps({
      "sender": user,
      "message": question
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("response text", response.text)
    value = json.loads(response.text)
    print("json", value)
    if value and len(value) != 0 and 'text' in value[0]:
        return value[0]['text']
    return "Watch your language!!! (rasa doesn't understand you, try adding GOOG anywhere to use google search)"



@app.route("/question")
def question():
    user = request.args.get('user')
    question = request.args.get('question')

    # temporary way to use both google and rasa,
    # should switch to rasa sending confidence
    use_google = 'GOOG' in question
    question = question.replace("GOOG", "")

    if use_google:
        return google(question)
    return rasa(user, question)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

