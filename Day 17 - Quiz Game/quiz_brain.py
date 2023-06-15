class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        player_answer = input(f"Q{self.question_number}: {current_question.text}")

        if self.check_answer(player_answer, correct_answer):
            print("Correct!")
            self.score += 1
        print(f"Score is: {self.score}/{self.question_number}")


    def check_answer(self, player_answer, correct_answer):
        return player_answer == correct_answer





