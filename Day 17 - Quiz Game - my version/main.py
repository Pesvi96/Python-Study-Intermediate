from quiz_brain import QuizBrain

quiz = QuizBrain()
power = True

while power:
    quiz.play()
    play_again = input(f"Wanna play again? Type 'y' or 'n' ").lower()
    while play_again not in ["y", "n"]:
        play_again = input(f"Wrong input, try again ")
    if play_again == "n":
        power = False
        print("Bye!")
