from quiz_brain import QuizBrain




quiz = QuizBrain()
power = True


while power:
    quiz.play()
    if not quiz.play_again():
        power = False
        print("Bye!")
