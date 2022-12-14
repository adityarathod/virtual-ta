from flask import Flask, request
from flask_cors import CORS
from googlesearch import search
import requests
import json
import random
from transformers import pipeline

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
    "how to",
    "can i",
    "?"
]

question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

context = r"""
Homework assignments are worth 27% of the course grade.
There will be approximately 6 homework assignments, they will include a combination of problem sets (of a sort) and programming.
Since we will be using Gradescope for submission and grading, you must upload an electronic copy of your assignment by the due date.
If you choose not to typewrite your assignment, you will need to scan and upload your submission.
Term project are worth 15% of the course grade.
There will be a term project due at the end of the semester.
The project is intended to provide you with hands-on experience with applying machine learning techniques to a research problem.
Midterm exams are worth 34% of the course grade total, which will be two midterm exams, tentatively scheduled on Oct 5, and the second on Nov 16.
Final exam is worth 24% of the course grade, which will be a comprehensive final exam during the final exam period.'''
"""


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

    use_syllabus = 'SYL' in question
    question = question.replace('SYL', '')

    if use_syllabus:
        return question_answerer(question=question, context=context)['answer']
    elif use_google:
        return stackoverflow(question)
    return rasa(user, question)


if __name__ == '__main__':
    app.run(port=5000)

