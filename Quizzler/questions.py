import requests
import html

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data = response.json()['results']


class Question:
    def __init__(self):
        self.n_question = 0
        self.question_number = 0

    def set_question(self):
        self.question = html.unescape(data[self.n_question]["question"])
        self.answer = html.unescape(data[self.n_question]["correct_answer"])

    def get_question(self):
        self.set_question()
        return self.question

    def next_question(self, score):
        if self.n_question < 10:
             self.n_question += 1
             self.set_question()
             return self.question
        else:
            return f"End of questions. Thank You for studying with our tool. This is your final score:\n {score}/10"
