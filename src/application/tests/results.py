# Showing all problems worked on by user
# Milton
from tkinter import *
import time
from src.application.views import math_screen
from pathlib import Path
import json
from datetime import datetime


def save_results(questions_list, student_id):
    path = f'{Path().absolute()}\\{student_id}_results.json'

    # Load existing results
    # Results are saved in the following form:
    # {'datetime0': [question0, question1], 'datetime1': [question0, question1]}
    try:
        with open(path) as file:
            json_results = json.load(file)
    except FileNotFoundError:
        json_results = {}

    # Get new results
    questions_json = []
    for question in questions_list:
        questions_json.append(question.to_dict())

    # Add new results
    json_results[str(datetime.now())] = questions_json
    with open(path, 'w') as file:
        json.dump(json_results, file)


# Frame
class LinksFrame(Frame):
    def __init__(self, parent, problems, student_id, **kwargs):
        super().__init__(parent, **kwargs)
        self.problems = problems

        # List and print all problem set grades.
        if len(self.problems.questions_list) > 0:
            self.index = 0
            self.incorrect_answers = 0
            self.correct_answers = 0
            for question in self.problems.questions_list:
                self.index += 1
                if question.student_correct():
                    self.text = f"Question {self.index}: {question.text} --- " \
                           f"Student Answer: {question.student_answer}. " \
                           f"Correct!"
                    self.correct_answers += 1
                else:
                    self.incorrect_answers += 1
                    self.text = f"Question {self.index}: {question.text} --- " \
                           f"Student Answer: {question.student_answer}. " \
                           f"Incorrect! " \
                           f"Correct Answer: {question.correct_answer}"
                Label(self, text=self.text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
                """
                if len(problems.math_screen.all_questions_list[x]) >= problems.math_screen.Total_Questions:
                    Label(self, text=f"Question {x + 1}: {problems.math_screen.all_questions_list[x][0]} --- "
                                     f"Student Answer: {problems.math_screen.all_questions_list[x][1]}. "
                                     f"{problems.math_screen.all_questions_list[x][2]}.",
                          wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
                else:
                    Label(self, text=f"Question {x + 1}: {problems.math_screen.all_questions_list[x][0]} --- "
                                     f"Student Answer: {problems.math_screen.all_questions_list[x][1]}. "
                                     f"CORRECT.",
                          wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
                """
            # Look for uncompleted questions
            self.total_questions = self.problems.Total_Questions
            self.incomplete_questions = self.total_questions - (self.correct_answers + self.incorrect_answers)
            if self.incomplete_questions != 0:
                if self.incomplete_questions == 1:
                    self.text = "1 question was not answered."
                else:
                    self.text = f"{self.incomplete_questions} questions were not answered."
                Label(self, text=self.text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

            # Give the score
            self.score = round((self.correct_answers / self.total_questions) * 100, 1)
            self.score_text = f"Assignment grade is {self.score:g}%"
            Label(self, text=self.score_text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

            save_results(self.problems.questions_list, student_id)

        else:
            Label(self, text=f"You did no questions. Grade: 0%",
                  wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)


# Results screen
class ResultsScreen(Tk):
    def __init__(self, ms, student_id, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.LinksFrame = LinksFrame(self, ms, student_id)
        self.LinksFrame.grid()


if __name__ == "__main__":
    ms_window_id = '1-ADD'
    ms_window = math_screen.Math_Screen_Settings(ms_window_id)
    # ms_window.geometry("600x500")
    ms_window.resizable(width=False, height=False)

    ms_window.mainloop()
    Results = ResultsScreen(ms_window.math_screen, 'test')
    Results.mainloop()
