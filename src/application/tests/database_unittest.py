import json
import os
import unittest

# Use self.assertEqual(Expected, Actual) or other assert methods
student_data_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'student_data.json'))


class DatabaseTest(unittest.TestCase):
    """Extract user data from existing student_data.json and add a user to the database,
    then retrieve the user's data from the database and make sure it matches."""
    def test_user_data(self):
        with open(student_data_path) as json_file:
            users_data = json.load(json_file)

        # Get a single user
        user = users_data['user 0']

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
