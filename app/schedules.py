import requests
import json

def display_feed(team="Bucks"):
    request_url = f"https://api-nba-v1.p.rapidapi.com/games"

    querystring = {"season":"2022","team":"1"}
    
    headers = {
	  "X-RapidAPI-Key": "d7f5a3d00dmsh6e9d7042e9a3dccp163db9jsn59e8d3fd2b59",
	  "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    
    response = requests.request("GET", request_url, params=querystring)
    
    data = json.loads(response.text)
    print(type(data)) #> dict
    print(data.keys())