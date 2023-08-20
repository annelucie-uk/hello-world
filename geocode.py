import requests

url = "https://trueway-geocoding.p.rapidapi.com/Geocode"

querystring = {"address":"11 Frosty Hollow, NN4 0SY","language":"en"}

headers = {
	"X-RapidAPI-Key": "a8182482d6msh5bdb45f8c4ffa5ep1f84e6jsn5cfb45bda4b5",
	"X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
\
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

print(response.json())

local_time_now = response.json()['LocalTime_Now']
print(local_time_now)
