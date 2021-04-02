import sqlite3
import sys

db_path = 'test.db'


def _create_user_table(cur):
    """Returns None if successful, returns error message if not."""
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS users'
                    '(username text COLLATE NOCASE, password text, child_first_name text, child_last_name text, '
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
    """Adds a user to the database. Returns 'Success' if user was saved, or an error message if not."""
    message = 'User could not be saved.'

    if not is_valid_username(user_info['username']):
        message = 'Invalid username'
        return message
    if not is_valid_password(user_info['password']):
        message = 'Invalid password'
        return message

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    e = _create_user_table(cur)
    if e is not None:
        con.close()
        return e

    username = user_info['username']
    # Make sure the username is not taken
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
        except sqlite3.DatabaseError:
            message = sys.exc_info()[1]
        else:
            message = 'Success'
    else:
        message = 'Username taken'

    con.commit()
    con.close()
    return message


def login(username, password):
    """Retrieves the user's data and returns a dictionary, or an error message if unsuccessful."""
    message = 'User could not be retrieved'

    username = username.strip()

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = 'SELECT username, child_first_name, child_last_name, child_grade, child_age, ' \
          'guardian_1_first_name, guardian_1_last_name, ' \
          'guardian_2_first_name, guardian_2_last_name ' \
          'FROM users WHERE username=? and password=?'
    try:
        cur.execute(sql, (username, password))
    except sqlite3.DatabaseError:
        message = sys.exc_info()[1]
        con.close()
        if message.args[0] == 'no such table: users':
            message = 'No users are registered'
        return message
    data = cur.fetchall()

    # Convert to dictionary
    user_dict = {}
    if len(data) == 1:
        user_raw = data[0]
        user_dict = {
            "username": user_raw[0],
            "child_first_name": user_raw[1],
            "child_last_name": user_raw[2],
            "child_grade": user_raw[3],
            "child_age": user_raw[4],
            "guardian_1_first_name": user_raw[5],
            "guardian_1_last_name": user_raw[6],
            "guardian_2_first_name": user_raw[7],
            "guardian_2_last_name": user_raw[8]}
        message = 'Success'
    elif len(data) == 0:
        if _user_exists(cur, username):
            message = 'Incorrect password'
        else:
            message = 'User does not exist'
    else:
        message = 'Duplicate users found'

    con.close()
    if user_dict != {}:
        return user_dict
    else:
        return message


# TODO: Add table for quiz results


# This is used for testing purposes
if __name__ == '__main__':
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

    print(add_user(all_information))
    print(login('genericusername ', 'secret'))
