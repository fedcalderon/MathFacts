# Stats graph page
# More things can be added to the file to show their progress on each problem
import os

import matplotlib.pyplot as plt
import tkinter as tk
import matplotlib.ticker as mtick
import src.application.models.database as db

graph_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'view_images', 'results_graph.png'))


class ReportsGraph:
    def configure_results_graph(self, username):
        # key_list = []
        # key_score_avg = []
        quizzes, message = db.get_every_quiz(username)

        print(quizzes)

        # quiz_scores is a dictionary with the following form: {quiz_type: {time: score, time: score...}, quiz_type:...}
        quiz_scores = {}
        for test_time, quiz in quizzes.items():
            quiz_type = quiz[0].type
            correct = 0
            total_questions = 0
            for question in quizzes[test_time]:
                total_questions += 1
                if question.student_correct():
                    correct += 1

            percentage_score = (correct / total_questions) * 100
            try:
                quiz_scores[quiz_type][test_time] = percentage_score
            except KeyError:
                quiz_scores[quiz_type] = {test_time: percentage_score}

        if len(quiz_scores) == 0:
            # If there are no quizzes, remove the file
            if os.path.exists(graph_path):
                os.remove(graph_path)
            return

        # print(key_list)
        # print(key_score_avg)
        # fig = plt.figure(figsize=(8, 6), dpi=80)
        # plt.xticks(rotation=30)
        # plt.plot(key_list, key_score_avg, 'o-')

        # Calculate number of rows and columns
        num_plots = len(quiz_scores)
        if num_plots > 1:
            cols = 2
            width = 9
        else:
            cols = 1
            width = 6

        rows = num_plots / 2
        if rows == int(rows):
            rows = int(rows)
        else:
            rows = int(rows + 0.5)
        if rows == 1:
            height = 4
        else:
            height = 6
        # print(f'{rows}, {cols}')

        index = 1
        fig = plt.figure(figsize=(width, height), facecolor=(0.94, 0.94, 0.94))
        for quiz_type, scores in quiz_scores.items():
            ax = plt.subplot(rows, cols, index)
            plt.ylim(top=101)
            if len(scores) == 1:
                xvalue = list(scores.keys())[0]
                ax.xaxis.set_ticks([xvalue])
                ax.xaxis.set_ticklabels([xvalue.strftime('%Y-%m-%d')])
            # Source: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent
            ax.yaxis.set_major_formatter(mtick.PercentFormatter())
            plt.plot(scores.keys(), scores.values(), '.-')
            plt.xticks(rotation=35)
            plt.ylabel(f'Scores of {quiz_type} quizzes')
            index += 1

        os.makedirs(os.path.dirname(graph_path), exist_ok=True)
        plt.tight_layout()
        plt.savefig(graph_path)
        plt.close(fig)

    def generate_graph(self, parent):
        self.configure_results_graph(parent.student_id)
        # plt.show()
        # parent.destroy()
        # parent.__init__()
        # parent.change_screen(parent.reports_screen)
