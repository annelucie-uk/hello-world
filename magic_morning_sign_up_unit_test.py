import unittest
import sqlite3

from magic_morning.py import sign_up

# Unit test for the sign_up function
class TestSignUpFunction(unittest.TestCase):
    def setUp(self):
        # Set up an in-memory SQLite database and cursor
        self.conn = sqlite3.connect(":memory:")
        self.c = self.conn.cursor()

        # Create the 'users' table
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                          (username TEXT PRIMARY KEY, password TEXT, date_of_birth TEXT, interests TEXT, daily_agenda TEXT)''')

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_successful_sign_up(self):
        # Test successful sign-up with valid user information
        username = "test_user"
        password = "test_password"
        date_of_birth = "1990-01-01"
        interests = "programming,reading,music"
        daily_agenda = "work,gym,study"

        # Call the function being tested
        sign_up(username, password, date_of_birth, interests, daily_agenda)

        # Verify the data is correctly inserted into the database
        self.c.execute("SELECT * FROM users WHERE username=?", (username,))
        user_data = self.c.fetchone()
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data[0], username)
        self.assertEqual(user_data[1], password)
        self.assertEqual(user_data[2], date_of_birth)
        self.assertEqual(user_data[3], interests)
        self.assertEqual(user_data[4], daily_agenda)

    def test_existing_username(self):
        # Test sign-up with an existing username
        username = "existing_user"
        password = "test_password"
        date_of_birth = "1990-01-01"
        interests = "programming,reading,music"
        daily_agenda = "work,gym,study"

        # Insert a user with the same username
        self.c.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                       (username, "other_password", date_of_birth, interests, daily_agenda))
        self.conn.commit()

        # Call the function being tested
        with self.assertRaisesRegex(Exception, f"The username {username} is already taken. Please choose a different username."):
            sign_up(username, password, date_of_birth, interests, daily_agenda)

    def test_missing_information(self):
        # Test sign-up with missing information
        # In this case, the username is not provided
        username = ""
        password = "test_password"
        date_of_birth = "1990-01-01"
        interests = "programming,reading,music"
        daily_agenda = "work,gym,study"

        # Call the function being tested
        with self.assertRaisesRegex(Exception, "One or more required fields are missing."):
            sign_up(username, password, date_of_birth, interests, daily_agenda)

if __name__ == '__main__':
    unittest.main()
