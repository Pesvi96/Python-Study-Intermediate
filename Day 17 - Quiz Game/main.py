from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []

for x in question_data:
    new_question = Question(x["text"], x["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Game finished")