import sqlite3
import sys
from datetime import datetime
from src.application.models.question import Question
import os

db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'MathFactsData.db'))


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


def _user_exists(cur, username, password=None):
    """Tells if the specified user exists. Optional password parameter."""
    try:
        if password is None:
            cur.execute('SELECT EXISTS(SELECT 1 FROM users WHERE username=?)', [username])
        else:
            cur.execute('SELECT EXISTS(SELECT 1 FROM users WHERE username=? and password=?)', (username, password))
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
    """Retrieves the user's data and returns it in a dictionary. The user's password is omitted from the dictionary.
    Message returns an error message if unsuccessful, or 'Success'.
    :param username: Case insensitive username.
    :param password: Case sensitive password.
    :returns: (user_dict, message)"""
    message = 'User could not be retrieved'

    user_dict = {}
    if username is None or password is None:
        return user_dict, 'User not found'
    username = username.strip()

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    try:
        cur.execute('SELECT * FROM users WHERE username=? and password=?', (username, password))
    except sqlite3.DatabaseError:
        message = sys.exc_info()[1]
        if message.args[0] == 'no such table: users':
            message = 'User not found'
        else:
            message = str(message)
    else:
        data = cur.fetchall()

        # Convert to dictionary
        if len(data) == 1:
            user_raw = data[0]
            user_dict = {
                "username": user_raw[0],
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
                message = 'User not found'
        else:
            message = 'Duplicate users found'

    con.close()
    return user_dict, message


def update_user_data(username, password, new_user_info):
    """Updates the user's data. Changes username and/or password if changed in the dictionary.
    Returns an error message if unsuccessful, or 'Success'.
    :param username: Current username (before update).
    :param password: Current password (before update).
    :param new_user_info: Dictionary containing the new user info. Does not need to include username or password.
    :returns: message"""
    message = 'User data could not be updated'

    # If the new username or password is blank, assume the user does not want to change it
    try:
        new_username = new_user_info['username']
    except KeyError:
        new_username = username
    if new_username is None or new_username == "":
        new_username = username

    try:
        new_password = new_user_info['password']
    except KeyError:
        new_password = password
    if new_password is None or new_password == "":
        new_password = password

    # Make sure the new username and password values are valid
    if not is_valid_username(new_username):
        message = 'Invalid username'
        return message
    if not is_valid_password(new_password):
        message = 'Invalid password'
        return message

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    if _user_exists(cur, username, password):
        child_fn = new_user_info['child_first_name']
        child_ln = new_user_info['child_last_name']
        child_grade = new_user_info['child_grade']
        child_age = new_user_info['child_age']
        g1_fn = new_user_info['guardian_1_first_name']
        g1_ln = new_user_info['guardian_1_last_name']
        g2_fn = new_user_info['guardian_2_first_name']
        g2_ln = new_user_info['guardian_2_last_name']
        # SQLite update statement: https://www.sqlitetutorial.net/sqlite-update/
        sql = 'UPDATE users SET username=?, password=?, child_first_name=?, child_last_name=?, ' \
              'child_grade=?, child_age=?, ' \
              'guardian_1_first_name=?, guardian_1_last_name=?, ' \
              'guardian_2_first_name=?, guardian_2_last_name=? WHERE username=? and password=?'
        try:
            cur.execute(sql, (new_username, new_password, child_fn, child_ln,
                              child_grade, child_age,
                              g1_fn, g1_ln, g2_fn, g2_ln, username, password))
            message = 'Success'
        except sqlite3.DatabaseError:
            message = str(sys.exc_info()[1])
        else:
            # If the username changed, update the username in the other tables
            if new_username != username:
                try:
                    cur.execute('UPDATE results SET username=? WHERE username=?', (new_username, username))
                except sqlite3.DatabaseError:
                    e = str(sys.exc_info()[1])
                    # If the table doesn't exist, just keep going
                    if e != 'no such table: results':
                        message = e
                try:
                    cur.execute('UPDATE settings SET username=? WHERE username=?', (new_username, username))
                except sqlite3.DatabaseError:
                    e = str(sys.exc_info()[1])
                    # If the table doesn't exist, just keep going
                    if e != 'no such table: settings':
                        message = e
            # If the username or password changed, update the remembered user
            if new_username != username or new_password != password:
                try:
                    sql = 'UPDATE app_vars SET value=? WHERE key=? and value=?'
                    cur.execute(sql, (new_username, 'remembered_username', username))
                    cur.execute(sql, (new_password, 'remembered_password', password))
                except sqlite3.DatabaseError:
                    e = str(sys.exc_info()[1])
                    if e != 'no such table: settings':
                        message = e
    elif _user_exists(cur, username):
        message = 'Incorrect password'
    else:
        message = 'User does not exist'

    con.commit()
    con.close()
    return message


def remove_user(username, password):
    """Removes the user from the database, including their quiz results and settings.
    Returns 'Success' if user was removed, or an error message if not."""
    message = 'User could not be removed.'

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Make sure the username and password are correct. We don't want to let anyone go around deleting all the accounts!
    if _user_exists(cur, username, password):
        message = 'Success'
        try:
            cur.execute('DELETE FROM results WHERE username=?', [username])
        except sqlite3.DatabaseError:
            pass
        try:
            cur.execute('DELETE FROM settings WHERE username=?', [username])
        except sqlite3.DatabaseError:
            pass
        try:
            cur.execute('DELETE FROM users WHERE username=?', [username])
        except sqlite3.DatabaseError:
            message = str(sys.exc_info()[1])
    else:
        if _user_exists(cur, username):
            message = 'Incorrect password'
        else:
            message = 'User does not exist'

    con.commit()
    con.close()
    return message


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
        return str(e)

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

    if _user_exists(cur, username):
        try:
            # SQLite replace statement: https://www.sqlitetutorial.net/sqlite-replace-statement/
            cur.execute('UPDATE settings SET num_problems=? WHERE username=?', (
                settings_dict['num_problems'], username))
            message = 'Success'
        except sqlite3.DatabaseError:
            message = str(sys.exc_info()[1])
    else:
        message = 'User does not exist'

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
            message = 'User settings not found'
        else:
            message = 'Duplicate users found'

    con.close()
    return settings_dict, message


def _create_app_vars_table(cur):
    """Returns None if successful, returns error message if not."""
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS app_vars('
                    'key text UNIQUE COLLATE NOCASE, value text)')
    except sqlite3.DatabaseError:
        return sys.exc_info()[1]


def set_remembered_user(username, password):
    """Sets the remembered user to the specified user and removes any previous remembered user.
    Returns 'Success' if settings were saved, or an error message if not."""
    message = 'Remembered user could not be saved'
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    e = _create_app_vars_table(cur)
    if e is not None:
        con.close()
        return str(e)

    if _user_exists(cur, username, password):
        try:
            # SQLite replace statement: https://www.sqlitetutorial.net/sqlite-replace-statement/
            cur.execute('REPLACE INTO app_vars VALUES("remembered_username", ?)', [username])
            cur.execute('REPLACE INTO app_vars VALUES("remembered_password", ?)', [password])
            message = 'Success'
        except sqlite3.DatabaseError:
            message = str(sys.exc_info()[1])
    else:
        message = 'User does not exist'

    con.commit()
    con.close()
    return message


def get_remembered_user():
    """Gets the remembered user's username and password.
    Message returns an error message if unsuccessful, or 'Success'.

    :returns: (remembered_username, remembered_password, message)"""
    message = 'Could not retrieve settings'
    remembered_username = None
    remembered_password = None
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    try:
        cur.execute('SELECT * FROM app_vars WHERE key=? or key=?', ('remembered_username', 'remembered_password'))
    except sqlite3.DatabaseError:
        message = sys.exc_info()[1]
        if message.args[0] == 'no such table: app_vars':
            message = 'No remembered users'
        else:
            message = str(message)
    else:
        data = cur.fetchall()
        message = 'Success'

        # Convert to dictionary
        if len(data) == 2:
            for row in data:
                if row[0] == 'remembered_username':
                    remembered_username = row[1]
                    if remembered_username == '':
                        remembered_username = None
                        message = 'No remembered user'
                elif row[0] == 'remembered_password':
                    remembered_password = row[1]
                    if remembered_password == '':
                        remembered_password = None
                        message = 'No remembered user'
        else:
            message = 'No remembered user'

    con.close()
    return remembered_username, remembered_password, message


def forget_remembered_user():
    """Forgets the remembered user.
    Returns 'Success' if user was forgotten, or an error message if not."""
    message = 'Remembered user could not be removed.'
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    try:
        cur.execute('DELETE FROM app_vars WHERE key="remembered_username" or key="remembered_password"')
        message = 'Success'
    except sqlite3.DatabaseError:
        message = str(sys.exc_info()[1])

    con.commit()
    con.close()
    return message


# This is used for testing/demo purposes
if __name__ == '__main__':
    # Sample user
    user_info = {
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
    username = 'GeneriCUsernamE'

    print("add_user:")
    print(add_user(user_info))
    print('login:')
    print(login(username, 'secret'))

    new_user_info = {
        "child_first_name": 'New',
        "child_last_name": 'Name',
        "child_grade": 4,
        "child_age": 10,

        "guardian_1_first_name": 'Another',
        "guardian_1_last_name": 'Guardian',

        "guardian_2_first_name": '',
        "guardian_2_last_name": '',

        "username": 'DifferentUsername',
        "password": 'Secret',
    }
    new_username = 'diFFerentuserNAME'

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
    print(save_results(username, question_list))
    print('get_every_quiz:')
    print(get_every_quiz(username))
    # print('get_every_question:')
    # print(get_every_question(username))
    # print('get_latest_quiz:')
    # print(get_latest_quiz(username))

    settings = {
        'num_problems': 50,
    }

    print('get_user_settings:')
    print(get_user_settings(username))
    print('save_user_settings:')
    print(save_user_settings(username, settings))

    # print('update_user_data:')
    # print(update_user_data(username, 'secret', new_user_info))

    # print('login (old username):')
    # print(login(username, 'secret'))
    # print('login (new username):')
    # print(login(new_username, 'Secret'))
    # print('get_every_quiz (old username):')
    # print(get_every_quiz(username))
    # print('get_every_quiz (new username):')
    # print(get_every_quiz(new_username))
    # print('get_user_settings (old username):')
    # print(get_user_settings(username))
    # print('get_user_settings (new username):')
    # print(get_user_settings(new_username))

    print('get_remembered_user:')
    print(get_remembered_user())
    print('set_remembered_user:')
    print(set_remembered_user(username, 'secret'))
    print('get_remembered_user:')
    print(get_remembered_user())
    print('remove_remembered_user:')
    print(forget_remembered_user())
    print('get_remembered_user:')
    print(get_remembered_user())
