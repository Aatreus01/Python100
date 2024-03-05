from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

i = 0

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))


