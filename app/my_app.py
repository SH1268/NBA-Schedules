print("it works")

def format_schedule(team):
    """
    Formatting for the team selected
    """
    return f"{team:.2f}%"

def fetch_data():
    """Fetches data from team"""
    request_url = "https://api-nba-v1.p.rapidapi.com/games"
