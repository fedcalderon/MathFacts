# Showing all problems worked on by user
# Milton
from tkinter import *
from pathlib import Path
import json
from datetime import datetime

import src.application.models.modified_logger as logger



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
        self.score = 0
        Label(self, text='GRADES:', wraplength=400, font=("TkDefaultFont", 20)).grid(sticky=W)

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

            # Log the task name and the score
            self.logger = logger.Logger('user_grades.log')
            self.logger.write_to_log(f"Completed task {self.problems.questions.ID} on {datetime.now()}. "
                                        f"Score is {self.score:g}")

            Label(self, text=self.score_text, wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
            save_results(self.problems.questions_list, student_id)

        else:
            Label(self, text=f"You did no questions. Grade: 0%",
                  wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

        Button(self, text="Start a new exercise", command=lambda: parent.change_screen(
        [self], parent.problem_selection_screen)).grid()


# Results screen
class ResultsScreen(Tk):
    def __init__(self, ms, student_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Math Facts Results')

        self.LinksFrame = LinksFrame(self, ms, student_id)
        self.LinksFrame.grid()
