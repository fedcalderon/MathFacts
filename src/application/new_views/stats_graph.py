# Stats graph page
# More things can be added to the file to show their progress on each problem
import matplotlib.pyplot as plt


class ReportsGraph:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ay = self.fig.add_subplot(111)

        self.ay.set_xlim(0, 10)
        # This is the limit that I put on the number of problems
        self.ax.set_xlim(0, 10)
        plt.savefig('view_images/user_graph.png')

    def generate_graph(self, parent):
        plt.show()
        parent.destroy()
        parent.__init__()
        parent.change_screen(parent.current_screen, parent.reports_screen)
