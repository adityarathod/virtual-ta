from flask import Flask, request
from flask_cors import CORS
from googlesearch import search
import requests
import json
import random


app = Flask(__name__)
CORS(app)


FILLERS = [
    "Here is what I found for you on StackOverflow. ",
    "Great question, does this answer from StackOverflow help?",
    "That's an interesting question, let me show you what people on StackOverflow thought about it."
]

NO_ANSWER = [
    "That's a tough question. Unfortunately I don't have an answer for you, but I'll ask your professor for you!",
    "Wow great question. I couldn't find an answer for you, but I sent it over to your professor and they'll answer you soon!"
]

QUESTION_FAT = [
    "what is",
    "what are",
    "?"
]


def fetch_answer(so_question_id):
    api_call = f"https://api.stackexchange.com/2.3/questions/{so_question_id}/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody"
    response = requests.get(api_call).json()
    if len(response["items"]) == 0:
        return False
    return response["items"][0]["body"]

def google(question):
    so_question = next(search('site:stackoverflow.com ' + question, stop=1))
    so_question_id = so_question.split("/")[4]
    answer = fetch_answer(so_question_id)
    return f'The answer to {question} is {answer}'


def stackoverflow(question):
    question = question.lower()
    for fat in QUESTION_FAT:
        question = question.replace(fat, "")
    api_call = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={question}&site=stackoverflow&filter=withbody"
    response = requests.get(api_call).json()
    if len(response["items"]) == 0:
        return random.choice(NO_ANSWER)

    title = response["items"][0]["title"]
    question_body = response["items"][0]["body"]
    so_question_id = response["items"][0]["question_id"]

    answer = fetch_answer(so_question_id)
    if not answer:
        return random.choice(NO_ANSWER)

    return f'''
    {random.choice(FILLERS)}
    <hr />
    <h3 class='text-2xl font-bold'>Question</h3>
    <p class='font-bold'>{title}</p>
    {question_body}
    <hr />
    <h3 class='text-2xl font-bold'>Top Voted Answer</h3>
    {answer}'''



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
    value = json.loads(response.text)
    if value and len(value) != 0 and 'text' in value[0]:
        return value[0]['text']
    return "I couldn't find any answers for that :("



@app.route("/question")
def question():
    user = request.args.get('user')
    question = request.args.get('question')

    # temporary way to use both google and rasa,
    # should switch to rasa sending confidence
    use_google = 'GOOG' in question
    question = question.replace("GOOG", "")

    if use_google:
        return stackoverflow(question)
    return rasa(user, question)


if __name__ == '__main__':
    app.run(port=5000)

