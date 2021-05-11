# Stats graph page
# More things can be added to the file to show their progress on each problem
import matplotlib.pyplot as plt
import json
import src.application.models.database as db
import src.application.models.question as question


class ReportsGraph:

    def configure_results_graph(self, username):
        # A test for connecting the stats_graph to the results screen and test_results.json
        key_list = []
        key_score_avg = []
        # test_time, latest_quiz, message = db.get_latest_quiz("DifferentUsername")
        quizzes, message = db.get_every_quiz(username)

        correct = 0
        total_questions = 0
        print(quizzes)
        for test_time in quizzes:
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
        plt.plot(key_list, key_score_avg)
        plt.savefig('view_images/results_graph.png')

    def display_graph(self, parent):
        self.configure_results_graph(parent.get_remembered_user())
        plt.show()
        parent.destroy()
        parent.__init__()
        parent.change_screen(parent.reports_screen)


if __name__ == "__main__":
    # A test for connecting the stats_graph to the results screen and the database
    percentage_score = 0
    iterator = 0
    key_list = []
    key_score_avg = []
    # test_time, latest_quiz, message = db.get_latest_quiz("DifferentUsername")
    quizzes, message = db.get_every_quiz("jimmy145")

    correct = 0
    total_questions = 0
    print(quizzes)
    for test_time in quizzes:
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
    plt.plot(key_list, key_score_avg)
    plt.savefig('view_images/results_graph.png')
    plt.show()
    # print(users_data[key][0]['correct_answer'])
