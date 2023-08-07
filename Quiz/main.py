from question_model import Question
from data import question_data
from quiz_brain import Brain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))

quiz = Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your score is {quiz.score}/{quiz.question_number}")


