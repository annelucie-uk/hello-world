import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
    "X-RapidAPI-Key": "a8182482d6msh5bdb45f8c4ffa5ep1f84e6jsn5cfb45bda4b5",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Parse the JSON response
data = response.json()

# Get location details
location = data['location']['name']
region = data['location']['region']

# Get current weather details
current_data = data['current']
temp_c = current_data['temp_c']
if 9 < temp_c < 20:
	temp_type = 'cool'
if temp_c < 10:
	temp_type = 'nippy'
if temp_c < 19 <26:
	temp_type = 'warm'
wind_mph = current_data['wind_mph']
wind_dir = current_data['wind_dir']
humidity = current_data['humidity']
condition_text = current_data['condition']['text']
if condition_text == 'Sunny':
	weather_reminder = "So don't forget your sunglasses and SPF 15!"
feelslike_c = current_data['feelslike_c']

#Personal_Information

your_name = input("Enter your first name: ")
your_date_of_birh = input("Enter your date of birth in the DD/MM/YYYY format: ")


alexa_weather_report = f"Good morning {location}! Today in {region}, the weather is {condition_text}. {weather_reminder} The temperature is currently a {temp_type} {temp_c} degrees Celsius, but it feels like {feelslike_c} degrees. The wind is coming from the {wind_dir} at {wind_mph} miles per hour. The humidity level is at {humidity} percent."

print(alexa_weather_report)
