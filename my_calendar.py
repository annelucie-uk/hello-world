import sqlite3
from datetime import datetime

class EventManager:
    def __init__(self):
        self.conn = sqlite3.connect('calendar.db')
        self.cursor = self.conn.cursor()

    def add_event(self, string_date, string_time, title):
        date = datetime.strptime(string_date, '%Y-%m-%d').date()
        time = datetime.strptime(string_time, '%H:%M').time()
        self.cursor.execute("INSERT INTO events (date, time, title) VALUES (?, ?, ?)", (date, time, title))
        self.conn.commit()

    def delete_event(self, string_date, title):
        date_to_delete = datetime.strptime(string_date, '%Y-%m-%d').date()
        self.cursor.execute("DELETE FROM events WHERE date = ? AND title = ?", (date_to_delete, title))
        if self.cursor.rowcount > 0:
            print("Event deleted.")
        else:
            print("Event not found.")
        self.conn.commit()

    def print_events_on_date(self, string_date):
        date_to_search = datetime.strptime(string_date, '%Y-%m-%d').date()
        self.cursor.execute("SELECT date, time, title FROM events WHERE date = ?", (date_to_search,))
        events = self.cursor.fetchall()
        for event in events:
            print("Date:", event[0])
            print("Time:", event[1])
            print("Title:", event[2])
            print()

event_manager = EventManager()

string_date = input("Enter date to look up events (format: yyyy-MM-dd): ")
event_manager.print_events_on_date(string_date)
