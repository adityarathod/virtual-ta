from flask import Flask, request
from flask_cors import CORS
from googlesearch import search
import requests
import json


app = Flask(__name__)
CORS(app)


@app.route("/question")
def question():
    user = request.args.get('user')
    question = request.args.get('question')

    url = "https://8602-129-110-242-176.ngrok.io/webhooks/rest/webhook"

    payload = json.dumps({
      "sender": user,
      "message": question
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    value = response.text
    print("Response: ", value)

    return value

    so_question = next(search('site:stackoverflow.com ' + question, stop=1))
    so_question_id = so_question.split("/")[4]
    api_call = f"https://api.stackexchange.com/2.3/questions/{so_question_id}/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody"
    response = requests.get(api_call).json()
    answer = response["items"][0]["body"]
    return f'The answer to {question} is {answer}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

