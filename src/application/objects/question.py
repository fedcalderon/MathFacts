"""A class that stores a single question and the user's response."""
# Andrew


class Question:
    """Pass either a dictionary or the individual variables, not both."""
    def __init__(self, question_dict=None, question_type=None, first_num=None, second_num=None, symbol=None, correct_ans=None, student_ans=None, text=None):
        if question_dict is None or question_dict == {}:
            # Base the properties off the given variables
            self.type = question_type
            self.first_number = first_num
            self.second_number = second_num
            self.symbol = symbol
            self.correct_answer = correct_ans
            self.student_answer = student_ans
            self.text = text
        else:
            # Base the properties off the dictionary
            self.type = question_dict['type']
            self.first_number = int(question_dict['first_number'])
            self.second_number = int(question_dict['second_number'])
            self.symbol = question_dict['symbol']
            self.correct_answer = question_dict['correct_answer']
            self.student_answer = question_dict['student_answer']
            self.text = question_dict['text']

    def student_correct(self):
        if type(self.correct_answer) is int and type(self.student_answer) is int:
            if self.correct_answer == self.student_answer:
                return True
            else:
                return False
        # If either variable is not set, return None
        return None

    def to_dict(self):
        question_dict = {'type': self.type,
                         'first_number': self.first_number,
                         'second_number': self.second_number,
                         'symbol': self.symbol,
                         'correct_answer': self.correct_answer,
                         'student_answer': self.student_answer,
                         'text': self.text}
        return question_dict
