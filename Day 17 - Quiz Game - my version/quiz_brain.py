from question_model import Questions
from random import choice


def check_input(player_input, correct_inputs):
    while player_input not in correct_inputs:
        player_input = input(f"Wrong input. Type {', '.join(correct_inputs)}")
    return player_input


class QuizBrain:
    def __init__(self):
        self.questions_list = []
        self.player_score = 0
        self.round = 0

    def play(self):
        # Creates a list of question objects
        self.create_questions_object_list()

        # Actual play
        for x in range(len(self.questions_list)):
            current_question = choice(self.questions_list)

            text = current_question.text
            answer = current_question.answer

            player_answer = input(f"Question {x}: {text} ").lower()
            check_input(player_answer, ["true", "false"])
            print(f"Correct answer is {answer}")
            self.questions_list.remove(current_question)
            if player_answer == answer.lower():
                self.player_score += 1
            self.round += 1
            print(f"Ongoing score: {self.player_score}/{self.round}\n")

        print(f"\n\nEnd of game! Your last score was {self.player_score}/{self.round}\n")

    def create_questions_object_list(self):
        for x in range(Questions.QUESTION_DATA_LENGTH):
            question = Questions(x)
            self.questions_list.append(question)

    def play_again(self):
        play_again = input(f"Wanna play again? Type 'y' or 'n' ").lower()
        check_input(play_again, ["y", "n"])
        if play_again == "n":
            return False
