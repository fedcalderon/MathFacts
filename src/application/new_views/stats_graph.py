# Stats graph page
# More things can be added to the file to show their progress on each problem
import matplotlib.pyplot as plt
import src.application.models.database as db
from src.application.models import question
import os

graph_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'view_images', 'results_graph.png'))


class ReportsGraph:
    def configure_results_graph(self, username):
        key_list = []
        key_score_avg = []
        quizzes, message = db.get_every_quiz(username)

        print(quizzes)
        for test_time in quizzes:
            correct = 0
            total_questions = 0
            for question in quizzes[test_time]:
                total_questions += 1
                if question.student_correct():
                    correct += 1

            percentage_score = (correct / total_questions) * 100
            key_score_avg.append(percentage_score)
            key_list.append(test_time)

        print(key_list)
        print(key_score_avg)

        fig = plt.figure(figsize=(8, 6), dpi=80)
        plt.xticks(rotation=30)
        plt.plot(key_list, key_score_avg, 'o-')
        os.makedirs(os.path.dirname(graph_path), exist_ok=True)
        plt.savefig(graph_path)
        plt.close(fig)

    def generate_graph(self, parent):
        self.configure_results_graph(parent.student_id)
        # plt.show()
        # parent.destroy()
        # parent.__init__()
        # parent.change_screen(parent.reports_screen)
