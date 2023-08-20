CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    date_of_birth TEXT,
    interests TEXT,
    daily_agenda TEXT,
    address TEXT
);
