from question_model import Questions
from random import choice


class QuizBrain:
    def __init__(self):
        self.questions_list = []
        self.player_score = 0
        self.round = 0

    def play(self):
        # Creates a list of question objects
        for x in range(Questions.QUESTION_DATA_LENGTH):
            question = Questions(x)
            self.questions_list.append(question)

        # Actual play
        for x in range(len(self.questions_list)):
            current_question = choice(self.questions_list)

            text = current_question.text
            answer = current_question.answer

            player_answer = input(f"Question {x}: {text} ").capitalize()
            while player_answer not in ["True", "False"]:
                player_answer = input(f"Wrong input, please try again ").capitalize()
            print(f"Correct answer is {answer}")
            self.questions_list.remove(current_question)
            if player_answer == answer:
                self.player_score += 1
            self.round += 1
            print(f"Ongoing score: {self.player_score}/{self.round}\n")

        print(f"\n\nEnd of game! Your last score was {self.player_score}/{self.round}")