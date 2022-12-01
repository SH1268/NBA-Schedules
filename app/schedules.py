import requests

url = "https://api-nba-v1.p.rapidapi.com/games"

querystring = {"date":"2022-11-22" , "league":"standard", "season":"2022", "team":"1"}

headers = {
	"X-RapidAPI-Key": "d7f5a3d00dmsh6e9d7042e9a3dccp163db9jsn59e8d3fd2b59",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

def fetch_stocks_data(symbol):
    request_url = f"https://api-nba-v1.p.rapidapi.com/games?"

    df = read_csv(request_url)
    return df

if __name__ == "__main__":

    team = input("Please input a team name to see a game (default: 'Knicks'): ") or "Knicks"
    print("Team:", team)

    df = fetch_game_data(team)

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    df = read_csv(request_url)
    print(df.columns)
    print(df.head())
    #breakpoint()

    # CHALLENGE A:
    # print the latest closing date and price

    latest = df.iloc[0]

    #print(latest["timestamp"])
    #print(latest["close"])
    print("LATEST:", format_usd(latest["adjusted_close"]), "as of", latest["timestamp"])

    # Challenge B
    #
    # What is the highest high price (formatted as USD)?
    # What is the lowest low price (formatted as USD)?

    print("HIGH:", format_usd(df["high"].max()))
    print("LOW:", format_usd(df["low"].min()))







