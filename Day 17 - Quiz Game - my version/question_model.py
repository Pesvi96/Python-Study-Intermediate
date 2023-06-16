from data import question_data


class Questions:
    QUESTION_DATA = question_data
    QUESTION_DATA_LENGTH = len(question_data)

    def __init__(self, number):
        self.text = question_data[number]["text"]
        self.answer = question_data[number]["answer"]
