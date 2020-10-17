import random


available_questions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

while True:
    before = available_questions
    random.shuffle(available_questions)
    after = available_questions

    if(before[-1] == after[0]):
        after[0] = before[-1]
        before[-1] = after[0]

    print(available_questions)