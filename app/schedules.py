import requests
from app.alpha import API_KEY

url = "https://api-nba-v1.p.rapidapi.com/games"

querystring = {"date":"2022-11-22" , "league":"standard", "season":"2022", "team":"1"}

headers = {
	"X-RapidAPI-Key": "{API_KEY}",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
