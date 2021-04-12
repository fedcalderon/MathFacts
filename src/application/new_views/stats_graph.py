#Stats graph page
#More things can be added to the file to show their progress on each problem
import matplotlib.pyplot as plt
#
fig = plt.figure()
ax = fig.add_subplot(111)
ay = fig.add_subplot(111)

ay.set_xlim(0, 10)
#This is the limit that i put on the number of problems
ax.set_xlim(0, 10)
#shows the graph
plt.show()
