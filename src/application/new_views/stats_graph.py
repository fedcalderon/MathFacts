# Stats graph page
# More things can be added to the file to show their progress on each problem
import matplotlib.pyplot as plt
import json


class ReportsGraph:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ay = self.fig.add_subplot(111)

        self.ay.set_xlim(0, 10)
        # This is the limit that I put on the number of problems
        self.ax.set_xlim(0, 10)
        plt.savefig('view_images/user_graph.png')

    def display_graph(self, parent):
        plt.show()
        parent.destroy()
        parent.__init__()
        parent.change_screen(parent.current_screen, parent.reports_screen)

    # def generate_graph(self):


if __name__ == "__main__":

    # A test for connecting the stats_graph to the results screen and test_results.json
    with open('test_results.json', 'r') as jsonfile:
        percentage_score = 0
        iterator = 0
        key_list = []
        key_score_avg = []
        users_data = json.load(jsonfile)
        for key in users_data:
            # print(users_data[key])
            # for element in users_data[key]:
            while iterator < 3:
                if users_data[key][0]['correct_answer'] == users_data[key][0]['student_answer']:
                    percentage_score += (100 / 3)
                else:
                    percentage_score += 0
                if iterator == 3:
                    iterator = 0
                iterator += 1

            key_score_avg.append(percentage_score)
            key_list = [x for x in range(0, len(key_score_avg))]
            print(key_list)
            print(key_score_avg)

        fig = plt.figure()
        plt.plot(key_list, key_score_avg)
        plt.savefig('view_images/results_graph.png')
        plt.show()
        #print(users_data[key][0]['correct_answer'])

