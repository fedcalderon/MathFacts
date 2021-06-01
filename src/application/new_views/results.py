# Showing all problems worked on by user
# Milton
from datetime import datetime
import src.application.models.modified_logger as logger
from tkinter import *


# Frame
class LinksFrame(Frame):
    def __init__(self, parent, problems, student_id, **kwargs):
        super().__init__(parent, **kwargs)
        self.problems = problems
        self.score = 0

        # Configure the scrollbar
        # Source: https://stackoverflow.com/a/3092341/7432
        self.canvas = Canvas(self, borderwidth=0)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.frame = Frame(self.canvas)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame, tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.frame.bind("<Visibility>", self.fix_scroll)

        Label(self.frame, text='GRADES:', font=("TkDefaultFont", 20)).grid()

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
                Label(self.frame, padx=10, text=self.text, wraplength=600, font=("TkDefaultFont", 11)).grid(sticky=W)

            # Look for uncompleted questions
            self.total_questions = self.problems.Total_Questions
            self.incomplete_questions = self.total_questions - (self.correct_answers + self.incorrect_answers)
            if self.incomplete_questions != 0:
                if self.incomplete_questions == 1:
                    self.text = "1 question was not answered."
                else:
                    self.text = f"{self.incomplete_questions} questions were not answered."
                Label(self.frame, padx=10, text=self.text, wraplength=600, font=("TkDefaultFont", 11)).grid(sticky=W)

            # Give the score
            self.score = round((self.correct_answers / self.total_questions) * 100, 1)
            self.score_text = f"Assignment grade is {self.score:g}%"

            # Log the task name and the score
            self.logger = logger.Logger('user_grades.log')
            self.logger.write_to_log(f"Completed task {self.problems.questions.questions_type} on {datetime.now()}. "
                                     f"Score is {self.score:g}")

            Label(self.frame, padx=10, text=self.score_text, wraplength=600, font=("TkDefaultFont", 11)).grid(sticky=W)
            # save_results(self.problems.questions_list, student_id)

        else:
            Label(self.frame, padx=10, text=f"You did no questions. Grade: 0%",
                  wraplength=600, font=("TkDefaultFont", 11)).grid(sticky=W)

        Button(self.frame, text="Start a new exercise", command=lambda: parent.change_screen(
            parent.problem_selection_screen)).grid()

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def fix_scroll(self, event):
        if self.frame.winfo_height() > self.canvas.winfo_height():
            self.canvas.yview_scroll(-10, "pages")

    def _on_mousewheel(self, event):
        # Source: https://stackoverflow.com/a/17457843
        # Only scroll if the frame is taller than the canvas
        if self.frame.winfo_height() > self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


# Results screen
class ResultsScreen(Tk):
    def __init__(self, ms, student_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Math Facts Results')

        self.LinksFrame = LinksFrame(self, ms, student_id)
        self.LinksFrame.grid()
