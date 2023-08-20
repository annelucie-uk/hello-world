import unittest
from datetime import datetime
import sqlite3
import os

class TestEventManager(unittest.TestCase):
    TEST_DB_PATH = 'test_calendar.db'

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(cls.TEST_DB_PATH)
        cursor = cls.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS events (date DATE, time TIME, title TEXT)")
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.remove(cls.TEST_DB_PATH)

    def setUp(self):
        self.event_manager = EventManager(db_path=self.TEST_DB_PATH)

    def test_add_event(self):
        string_date = '2023-08-04'
        string_time = '10:00'
        title = 'Test Event'
        
        self.event_manager.add_event(string_date, string_time, title)

        cursor = self.conn.cursor()
        cursor.execute("SELECT date, time, title FROM events WHERE date = ? AND time = ? AND title = ?", (datetime.strptime(string_date, '%Y-%m-%d').date(), datetime.strptime(string_time, '%H:%M').time(), title))
        event = cursor.fetchone()

        self.assertIsNotNone(event)
        self.assertEqual(event[0], string_date)
        self.assertEqual(event[1], string_time)
        self.assertEqual(event[2], title)

    # You can also add tests for other methods here

if __name__ == '__main__':
    unittest.main()
