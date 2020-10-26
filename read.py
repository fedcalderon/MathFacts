score = 0
q_attempted = 0

"""example question"""
print('3 + 4 = ?')
q_attempted += 1

user_input = input('')

answer = 7
if user_input == 7:
    score += 1
    print('That is correct!')
else:
    print('That is incorrect.')


print('You have finished, your score is' + str(score) + '/' + str(q_attempted) + '.')