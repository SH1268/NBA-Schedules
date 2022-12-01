import requests

url = "https://api-nba-v1.p.rapidapi.com/games"

querystring = {"season":"2022", "team":"15", "date":"2022-11-10"}

headers = {
	"X-RapidAPI-Key": "d7f5a3d00dmsh6e9d7042e9a3dccp163db9jsn59e8d3fd2b59",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)