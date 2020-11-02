import random

# A a_list to test the function.
sample_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

# The randomize a_list function.
# 1. Takes one paramater(the a_list). Right now it just takes strings to represent the questions, but this can be changed
#    later on.
#
# 2. Randomizes the list and then returns it.


def randomize_list(a_list):
    #################################################################################
    # THE RANDOMIZING CODE
    before = a_list
    random.shuffle(before)

    after = a_list
    random.shuffle(after)

    #print(f"Before: {before}")
    #print(f"After: {after}")

    if(before[-1] == after[0]):
        after[0] = before[0]

    if(before[-2] == after[0]):
        after[0] = before[0]
    ##################################################################################

    return a_list

# If the user presses Y, then the function runs again.
#
# 2. Prints the a_list questions to the console for now(later, this can be changed to print them to the GUI instead).
#
# 3. A user will then type whether they want to continue or not. If they press yes, then randomize_list will run again.


while True:

    continueQuestions = input("Continue with another a_list of questions? (Y or N)")
    if(continueQuestions == "Y"):
        continue
    elif(continueQuestions == "N"):
        break

