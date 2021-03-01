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

        # List and print all problem set grades.
        if len(problems.math_screen.questions_list) > 0:
            index = 0
            incorrect_answers = 0
            correct_answers = 0
            for question in problems.math_screen.questions_list:
                index += 1
                if question.student_correct():
                    text = f"Question {index}: {question.text} --- " \
                           f"Student Answer: {question.student_answer}. " \
                           f"Correct!"
                    correct_answers += 1
                else:
                    incorrect_answers += 1
                    text = f"Question {index}: {question.text} --- " \
                           f"Student Answer: {question.student_answer}. " \
                           f"Incorrect! " \
                           f"Correct Answer: {question.correct_answer}"
                Label(self, text=text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
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
            total_questions = problems.math_screen.Total_Questions
            incomplete_questions = total_questions - (correct_answers + incorrect_answers)
            if incomplete_questions != 0:
                if incomplete_questions == 1:
                    text = "1 question was not answered."
                else:
                    text = f"{incomplete_questions} questions were not answered."
                Label(self, text=text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

            # Give the score
            score = round((correct_answers / total_questions) * 100, 1)
            score_text = f"Assignment grade is {score:g}%"
            Label(self, text=score_text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

            save_results(problems.math_screen.questions_list, student_id)

        else:
            Label(self, text=f"You did no questions. Grade: 0%",
                  wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

        # desc_label.grid()


# Results screen
class ResultsScreen(Tk):
    def __init__(self, ms, student_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.geometry("600x800")

        self.LinksFrame = LinksFrame(self, ms, student_id)
        #if len(ms_window.math_screen.all_questions_list) > 3:
        self.LinksFrame.grid()


if __name__ == "__main__":
    ms_window_id = '1-SUB'
    ms_window = math_screen.Math_Screen_Settings(ms_window_id)
    # ms_window.geometry("600x500")
    ms_window.resizable(width=False, height=False)

    ms_window.mainloop()
    Results = ResultsScreen(ms_window, 'test')
    Results.mainloop()
