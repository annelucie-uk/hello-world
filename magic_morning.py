import requests
import sqlite3
import datetime
from getpass import getpass
import random

# Connect to SQLite database (or create it)
conn = sqlite3.connect('user_preferences.db')
c = conn.cursor()

# Create table for user info and preferences if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, date_of_birth TEXT, interests TEXT, daily_agenda TEXT)''')

# Commit the changes
conn.commit()


def sign_up(username, password, date_of_birth, interests, daily_agenda):
    # Check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone() is not None:
        print(f"The username {username} is already taken. Please choose a different username.")
        return

    # Insert a row of user data
    c.execute("INSERT INTO users VALUES (?,?,?,?,?)", (username, password, date_of_birth, interests, daily_agenda))
    conn.commit()
    print("User created successfully!")


def sign_in():
    username = input("Please enter your username: ")
    password = getpass("Please enter your password: ")

    # Fetch user data
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user is None:
        print(f"No user found for username: {username} and password: {password}")
        return None

    return user

import requests

url = "https://trueway-geocoding.p.rapidapi.com/Geocode"

querystring = {"address":"11 Frosty Hollow, NN4 0SY","language":"en"}

headers = {
	"X-RapidAPI-Key": "a8182482d6msh5bdb45f8c4ffa5ep1f84e6jsn5cfb45bda4b5",
	"X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

latitude = response.json()['results'][0]['location']['lat']
longitude = response.json()['results'][0]['location']['lng']

url = "https://geocodeapi.p.rapidapi.com/GetTimezone"

querystring = {"latitude": latitude, "longitude": longitude}

headers = {
	"X-RapidAPI-Key": "a8182482d6msh5bdb45f8c4ffa5ep1f84e6jsn5cfb45bda4b5",
	"X-RapidAPI-Host": "geocodeapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



local_time_now = response.json()['LocalTime_Now']



def fetch_weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    coordinates = f"{latitude}, {longitude}"
    querystring = {"q": coordinates}
    headers = {
        "X-RapidAPI-Key": "a8182482d6msh5bdb45f8c4ffa5ep1f84e6jsn5cfb45bda4b5",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Get location details
    location = data['location']['name']
    region = data['location']['region']

    # Get current weather details
    current_data = data['current']
    temp_c = current_data['temp_c']

    # Temperature description
    if temp_c < 10:
        temp_type = 'a bit chilly'
    elif 10 <= temp_c < 20:
        temp_type = 'quite cool'
    elif 20 <= temp_c < 26:
        temp_type = 'rather warm'
    else:
        temp_type = 'quite hot'

    wind_mph = current_data['wind_mph']
    wind_dir = current_data['wind_dir']
    humidity = current_data['humidity']
    condition_text = current_data['condition']['text']

    # Weather condition reminder
    if condition_text.lower() == 'sunny':
        weather_reminder = "Don't forget your sunglasses and some sunscreen!"
    elif condition_text.lower() in ['rain', 'showers']:
        weather_reminder = "You might want to take an umbrella with you."
    elif condition_text.lower() in ['snow', 'sleet']:
        weather_reminder = "It's going to be slippery out there, so be careful!"
    else:
        weather_reminder = "Enjoy your day!"

    feelslike_c = current_data['feelslike_c']

    weather_report = f"Good morning! The time is {local_time_now}. Today in {location}, {region}, it's currently {condition_text}. {weather_reminder} \
    The temperature is {temp_c} degrees Celsius, but it feels like {feelslike_c} degrees. It's {temp_type} today. \
    The wind is coming from the {wind_dir} at {wind_mph} miles per hour, and the humidity level is at {humidity} percent."

    return weather_report



import random

def fetch_leo_quote():
    quotes = ["This week we're talking about how a lack of discipline makes you ugly.",
              "Even if someone's kind of ugly, if you respect them, you're going to want to be with them a little more.",
              "The only way you will begin to respect yourself is by going through hard stuff. There's no way around it; there's no way to get the sense of confidence and respect for yourself, or for anyone to get it without going through or doing some hard things.",
              "Having a nice body is just the most unspoken silent flex you can have because it's a silent way to display certain character traits.",
              "Being physically fit demands a certain respect, like your best accessory to an outfit is a nice body. I hate to say it, but it's the truth.",
              "Every single person you see with a good body has to do something for it, to maintain it, and to get it to look the way that it does. They don't just look good by accident.",
              "If I looked now the way I used to look, out of shape, I wouldn't be taken seriously. Like, having discipline and having a nice body makes you more credible.",
              "If the package matches the amount of value you can share, it's valued more, and it's more credible."]
    quote_of_the_day = random.choice(quotes)
    return quote_of_the_day

def main():
    user = sign_in()
    if user is not None:
        print("Welcome back, " + user[0] + "!")
        print(fetch_weather())
        daily_agenda = user[4]
        if daily_agenda:
            print("Your agenda for today:")
            for item in daily_agenda.split(','):
                print(" - " + item.strip())
        print("Remember ", fetch_leo_quote())


print("Welcome to the Magic Morning App. We're so excited to give you the wake up of your dreams.")

account_status = input("Do you already have an account with us? Please type yes or no.")
if account_status == 'yes':
    main()

if account_status == 'no':
    sign_up('user_test', 'pass_test', '1990-01-01', 'programming,reading,music', 'Tech Developer Programme at 10am, Train to Cambridge at 3pm, Birthday Party at 6pm')
    main()

# Close the connection
conn.close()
