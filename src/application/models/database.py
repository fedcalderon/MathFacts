import sqlite3
import sys
from datetime import datetime
from src.application.models.question import Question
import os


db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'test.db'))


def _create_user_table(cur):
    """Returns None if successful, returns error message if not."""
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS users'
                    '(username text UNIQUE COLLATE NOCASE, password text, child_first_name text, child_last_name text, '
                    'child_grade int, child_age int, '
                    'guardian_1_first_name text, guardian_1_last_name text, '
                    'guardian_2_first_name text, guardian_2_last_name text)')
    except sqlite3.DatabaseError:
        return sys.exc_info()[1]


def _user_exists(cur, username):
    try:
        cur.execute('SELECT EXISTS(SELECT 1 FROM users WHERE username=?)', [username])
    except sqlite3.DatabaseError:
        return False
    if cur.fetchone()[0] == 0:
        return False
    else:
        return True


def is_valid_username(username):
    for char in username:
        if char.isalnum():
            continue
        else:
            return False

    if len(username) == 0 or len(username) > 24:
        return False
    else:
        return True


def is_valid_password(password):
    if len(password) <= 3 or len(password) > 24:
        return False
    else:
        return True


def add_user(user_info):
    """Adds a user to the database, and saves default settings for the user.
    Returns 'Success' if user was saved, or an error message if not.
    Checks to make sure username is not already taken."""
    message = 'User could not be saved.'

    # Make sure the username and password values are valid
    if not is_valid_username(user_info['username']):
        message = 'Invalid username'
        return message
    if not is_valid_password(user_info['password']):
        message = 'Invalid password'
        return message

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Create tables
    e = _create_user_table(cur)
    if e is not None:
        con.close()
        return str(e)
    e = _create_settings_table(cur)
    if e is not None:
        con.close()
        return str(e)

    username = user_info['username']
    # Make sure the username is not taken, then add the values to the table
    if not _user_exists(cur, username):
        password = user_info['password']
        child_fn = user_info['child_first_name']
        child_ln = user_info['child_last_name']
        child_grade = user_info['child_grade']
        child_age = user_info['child_age']
        g1_fn = user_info['guardian_1_first_name']
        g1_ln = user_info['guardian_1_last_name']
        g2_fn = user_info['guardian_2_first_name']
        g2_ln = user_info['guardian_2_last_name']
        try:
            cur.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                username, password, child_fn, child_ln,
                child_grade, child_age,
                g1_fn, g1_ln, g2_fn, g2_ln))
            message = 'Success'
        except sqlite3.DatabaseError:
            message = str(sys.exc_info()[1])
        else:
            # Set default settings for the new user
            default_num_problems = 20
            try:
                cur.execute('INSERT INTO settings VALUES(?, ?)', (
                    username, default_num_problems))
            except sqlite3.DatabaseError:
                message = str(sys.exc_info()[1])
    else:
        message = 'Username taken'

    con.commit()
    con.close()
    return message


def login(username, password):
    """Retrieves the user's data and returns it in a dictionary.
    Message returns an error message if unsuccessful, or 'Success'.

    :param username: Case insensitive username.
    :param password: Case sensitive password.
    :returns: (user_dict, message)"""
    message = 'User could not be retrieved'

    username = username.strip()
    user_dict = {}

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    try:
        cur.execute('SELECT * FROM users WHERE username=? and password=?', (username, password))
    except sqlite3.DatabaseError:
        message = sys.exc_info()[1]
        if message.args[0] == 'no such table: users':
            message = 'No users are registered'
        else:
            message = str(message)
    else:
        data = cur.fetchall()

        # Convert to dictionary
        if len(data) == 1:
            user_raw = data[0]
            user_dict = {
                "username": user_raw[0],
                "password": user_raw[1],
                "child_first_name": user_raw[2],
                "child_last_name": user_raw[3],
                "child_grade": user_raw[4],
                "child_age": user_raw[5],
                "guardian_1_first_name": user_raw[6],
                "guardian_1_last_name": user_raw[7],
                "guardian_2_first_name": user_raw[8],
                "guardian_2_last_name": user_raw[9]}
            message = 'Success'
        elif len(data) == 0:
            if _user_exists(cur, username):
                message = 'Incorrect password'
            else:
                message = 'User does not exist'
        else:
            message = 'Duplicate users found'

    con.close()
    return user_dict, message


# TODO: Add a method to edit user data, change username, and change password


def _create_results_table(cur):
    """Returns None if successful, returns error message if not."""
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS results('
                    'username text COLLATE NOCASE, datetime timestamp, type text, '
                    'first_number int, second_number int, symbol text, '
                    'correct_answer int, student_answer int, question_text text)')
    except sqlite3.DatabaseError:
        return sys.exc_info()[1]


def save_results(username, questions):
    """Saves the results of a single quiz to the database.
    Returns 'Success' if the results were saved, or an error message if not."""
    test_time = datetime.now()
    message = 'Results not saved'

    con = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()

    e = _create_results_table(cur)
    if e is not None:
        con.close()
        return e

    # Make sure the username exists
    if _user_exists(cur, username):
        # Insert each question into the database
        for question in questions:
            try:
                cur.execute('INSERT INTO results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    username, test_time, question.type, question.first_number, question.second_number,
                    question.symbol, question.correct_answer, question.student_answer, question.text))
                message = 'Success'
            except sqlite3.DatabaseError:
                message = str(sys.exc_info()[1])
                break
    else:
        message = 'User does not exist'

    con.commit()
    con.close()
    return message


def _get_every_question_row(cur, username):
    sql = 'SELECT datetime, type, first_number, second_number, ' \
          'symbol, correct_answer, student_answer, question_text ' \
          'FROM results WHERE username=?'
    try:
        cur.execute(sql, [username])
    except sqlite3.DatabaseError:
        message = sys.exc_info()[1]
        if message.args[0] == 'no such table: results':
            message = {}
        else:
            message = str(message)
        return message
    return cur.fetchall()


def get_every_quiz(username):
    """Returns every quiz for the given user in a dict with the form {datetime: [question, question,...],...}.
    Message returns an error message if unsuccessful, or 'Success'.

    :returns: (quizzes, message)"""
    message = 'Could not retrieve results'

    con = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()

    quizzes = {}
    # Make sure the user exists
    if _user_exists(cur, username):
        # Find all questions for the given user
        data = _get_every_question_row(cur, username)
        if type(data) == str:
            # If it returns a string, it is an error message
            message = data
        else:
            for question_raw in data:
                # Make a new question object for each question retrieved
                question = Question()
                dt = question_raw[0]
                question.type = question_raw[1]
                question.first_number = question_raw[2]
                question.second_number = question_raw[3]
                question.symbol = question_raw[4]
                question.correct_answer = question_raw[5]
                question.student_answer = question_raw[6]
                question.text = question_raw[7]

                if dt in quizzes:
                    # Add to existing quiz
                    quizzes[dt].append(question)
                else:
                    # Make a new question list
                    quizzes[dt] = [question]
            message = 'Success'
    else:
        message = 'User does not exist'
    con.close()

    return quizzes, message


def get_every_question(username):
    """Returns a list of every question for the given user, regardless of which quiz the questions were a part of.
    Message returns an error message if unsuccessful, or 'Success'.

    :returns: (questions, message)"""
    message = 'Could not retrieve questions'

    con = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()

    questions = []
    # Make sure the user exists
    if _user_exists(cur, username):
        # Find all questions for the given user
        data = _get_every_question_row(cur, username)
        if type(data) == str:
            # If it returns a string, it is an error message
            message = data
        else:
            # Parse the data into the list of questions
            for question_raw in data:
                question = Question()
                question.type = question_raw[1]
                question.first_number = question_raw[2]
                question.second_number = question_raw[3]
                question.symbol = question_raw[4]
                question.correct_answer = question_raw[5]
                question.student_answer = question_raw[6]
                question.text = question_raw[7]

                questions.append(question)
            message = 'Success'
    else:
        message = 'User does not exist'
    con.close()

    return questions, message


def get_latest_quiz(username):
    """Gets the questions from the user's most recent quiz.
    Message returns an error message if unsuccessful, or 'Success'.

    :returns: (test_time, questions, message)"""
    message = 'Could not retrieve questions'

    con = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()

    test_time = None
    questions = []
    # Make sure the user exists
    if _user_exists(cur, username):
        # Find question from the user's most recent quiz
        sql = 'SELECT datetime, type, first_number, second_number, ' \
              'symbol, correct_answer, student_answer, question_text ' \
              'FROM results ' \
              'WHERE username=? and datetime=(SELECT MAX(datetime) FROM results WHERE username=?)'
        try:
            cur.execute(sql, (username, username))
        except sqlite3.DatabaseError:
            message = sys.exc_info()[1]
            if message.args[0] == 'no such table: results':
                message = 'User has not taken a quiz'
            else:
                message = str(message)
        else:
            # Parse the data into a list of questions
            data = cur.fetchall()

            test_time = data[0][0]
            for question_raw in data:
                question = Question()
                question.type = question_raw[1]
                question.first_number = question_raw[2]
                question.second_number = question_raw[3]
                question.symbol = question_raw[4]
                question.correct_answer = question_raw[5]
                question.student_answer = question_raw[6]
                question.text = question_raw[7]

                questions.append(question)
            if len(questions) != 0:
                message = 'Success'
            else:
                message = 'User has not taken a quiz'
    else:
        message = 'User does not exist'
    con.close()

    return test_time, questions, message


def _create_settings_table(cur):
    """Returns None if successful, returns error message if not."""
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS settings('
                    'username text UNIQUE COLLATE NOCASE, num_problems int)')
    except sqlite3.DatabaseError:
        return sys.exc_info()[1]


def save_user_settings(username, settings_dict):
    """Updates a user's settings. Returns 'Success' if settings were saved, or an error message if not."""
    message = 'Settings could not be saved.'
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    e = _create_settings_table(cur)
    if e is not None:
        con.close()
        return str(e)

    try:
        # Replace statement: https://www.sqlitetutorial.net/sqlite-replace-statement/
        cur.execute('REPLACE INTO settings VALUES(?, ?)', (
            username, settings_dict['num_problems']))
        message = 'Success'
    except sqlite3.DatabaseError:
        message = str(sys.exc_info()[1])

    con.commit()
    con.close()
    return message


def get_user_settings(username):
    """Gets the user's settings in the form of a dictionary.
    Message returns an error message if unsuccessful, or 'Success'.

    :returns: (settings_dict, message)"""
    message = 'Could not retrieve settings'
    settings_dict = {}
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    try:
        cur.execute('SELECT * FROM settings WHERE username=?', [username])
    except sqlite3.DatabaseError:
        message = sys.exc_info()[1]
        if message.args[0] == 'no such table: settings':
            message = 'No users have saved settings'
        else:
            message = str(message)
    else:
        data = cur.fetchall()

        # Convert to dictionary
        if len(data) == 1:
            settings_raw = data[0]
            settings_dict = {
                "num_problems": settings_raw[1]}
            message = 'Success'
        elif len(data) == 0:
            message = 'User not found'
        else:
            message = 'Duplicate users found'

    con.close()
    return settings_dict, message


# This is used for testing/demo purposes
if __name__ == '__main__':
    # Sample user
    all_information = {
        "child_first_name": 'Generic',
        "child_last_name": 'Student',
        "child_grade": 3,
        "child_age": 9,

        "guardian_1_first_name": 'Some',
        "guardian_1_last_name": 'Guardian',

        "guardian_2_first_name": '',
        "guardian_2_last_name": '',

        "username": 'GenericUsername',
        "password": 'secret',
    }

    username = 'genericusername'
    print("add_user:")
    print(add_user(all_information))
    print('login:')
    print(login(username, 'secret'))

    # Sample math questions
    question1 = Question(question_type='TEST',
                         first_num=5,
                         second_num=6,
                         symbol='+',
                         correct_ans=11,
                         student_ans=11,
                         text='What is 5 + 6?')
    question2 = Question(question_type='TEST',
                         first_num=8,
                         second_num=3,
                         symbol='+',
                         correct_ans=11,
                         student_ans=12,
                         text='What is 8 + 3?')
    question_list = [question1, question2]

    print('save_results:')
    print(save_results('genericusername', question_list))
    print('get_every_quiz:')
    print(get_every_quiz(username))
    print('get_every_question:')
    print(get_every_question(username))
    print('get_latest_quiz:')
    print(get_latest_quiz(username))

    settings = {
        'num_problems': 50,
    }

    print('get_user_settings:')
    print(get_user_settings(username))
    print('save_user_settings:')
    print(save_user_settings(username, settings))
    print('get_user_settings:')
    print(get_user_settings(username))
