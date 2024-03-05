from question_model import Question
from data import question_data

question_bank = []

i = 0

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

for question in question_bank:
    print(question.text, question.answer)
