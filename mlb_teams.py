import requests

url = (
    "https://statsapi.mlb.com/api/v1/teams"
    "?sportId=1"
)

resp = requests.get(url)
data = resp.json()

# Example: list dates and matchups
for date in data.get("teams", []):
    print(date["date"])
    for game in date["games"]:
        away = game["teams"]["away"]["team"]["name"]
        home = game["teams"]["home"]["team"]["name"]
        print(f"  {away} at {home}")

        #id, abbreviation, teamName, locationName, league[id], league[name], divistion[id,] division[name]