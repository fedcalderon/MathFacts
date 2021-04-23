import json
import os
import unittest
import src.application.models.database as database

# NOTE: the tests must be run in order for the tests to work since they depend on the state of the database
# This test uses data from 'user 0' in student_data.json


student_data_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'student_data.json'))
database.db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'unittest.db'))


# Use self.assertEqual(Expected, Actual) or other assert methods
class DatabaseTest(unittest.TestCase):
    def __init__(self, *args):
        """Extract user data from existing student_data.json and prepare it for the tests."""
        super().__init__(*args)
        with open(student_data_path) as json_file:
            users_data = json.load(json_file)

        # Get a single user
        self.user = users_data['user 0']
        self.username = self.user['username']
        self.password = self.user['password']

        # Convert the numbers from strings to integers
        self.user['child_age'] = int(self.user['child_age'])
        self.user['child_grade'] = int(self.user['child_grade'])

    def test_add_user(self):
        """Add the user to the database."""
        # Add the user to the database
        message = database.add_user(self.user)
        self.assertEqual('Success', message)

    def test_login(self):
        """Retrieve the user's data from the database and make sure it matches the data that was added."""
        # Login and make sure the user's data is retrieved correctly
        user_from_database, message = database.login(self.username, self.password)
        self.assertEqual('Success', message)

        # Remove the password from the dictionary since database.login doesn't return it
        del self.user['password']

        self.assertEqual(self.user, user_from_database)

    def test_remove_user(self):
        """Remove the user from the database."""
        # Remove the user to clean up the database and allow the test to be run multiple times
        message = database.remove_user(self.username, self.password)
        self.assertEqual('Success', message)

        # Make sure the user is gone
        d, message = database.login(self.username, self.password)
        self.assertEqual('User does not exist', message)


if __name__ == '__main__':
    unittest.main()
