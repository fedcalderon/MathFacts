# Stats graph page
# More things can be added to the file to show their progress on each problem
import matplotlib.pyplot as plt
import json
import src.application.models.database as db
import src.application.models.question as question


class ReportsGraph:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ay = self.fig.add_subplot(111)

        self.ay.set_xlim(0, 10)
        # This is the limit that I put on the number of problems
        self.ax.set_xlim(0, 10)
        plt.savefig('view_images/user_graph.png')

    def configure_results_graph(self):
        # A test for connecting the stats_graph to the results screen and test_results.json
        key_list = []
        key_score_avg = []
        # test_time, latest_quiz, message = db.get_latest_quiz("DifferentUsername")
        quizzes, message = db.get_every_quiz("GenericUsername")

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

    def display_graph(self, parent):
        plt.show()
        parent.destroy()
        parent.__init__()
        parent.change_screen(parent.current_screen, parent.reports_screen)

    # def generate_graph(self):


if __name__ == "__main__":
    # # A test for connecting the stats_graph to the results screen and test_results.json
    # with open('test_results.json', 'r') as jsonfile:
    #     percentage_score = 0
    #     iterator = 0
    #     key_list = []
    #     key_score_avg = []
    #     users_data = json.load(jsonfile)
    #     for key in users_data:
    #         # print(users_data[key])
    #         # for element in users_data[key]:
    #         while iterator < 20:
    #             if users_data[key][0]['correct_answer'] == users_data[key][0]['student_answer']:
    #                 percentage_score += (100 / 20)
    #             else:
    #                 percentage_score += 0
    #             if iterator == 20:
    #                 iterator = 0
    #             iterator += 1
    #
    #         key_score_avg.append(percentage_score)
    #         key_list = [x for x in range(0, len(key_score_avg))]
    #         print(key_list)
    #         print(key_score_avg)
    #
    #     fig = plt.figure()
    #     plt.plot(key_list, key_score_avg)
    #     plt.savefig('view_images/results_graph.png')
    #     plt.show()
    #     # print(users_data[key][0]['correct_answer'])

    # A test for connecting the stats_graph to the results screen and test_results.json
    percentage_score = 0
    iterator = 0
    key_list = []
    key_score_avg = []
    # test_time, latest_quiz, message = db.get_latest_quiz("DifferentUsername")
    quizzes, message = db.get_every_quiz("GenericUsername")

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

