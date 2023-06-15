from question_model import Question
from data import question_data

question_bank = []

for x in question_data:
    new_question = Question(x["text"], x["answer"])
    # question_bank.append((question.text, question.answer))
    question_bank.append(new_question)
print (question_bank)

