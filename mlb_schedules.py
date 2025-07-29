import requests, time
import pandas as pd

url = (
    "https://statsapi.mlb.com/api/v1/schedule"
    "?sportId=1"
    "&startDate=2025-03-29"
    "&endDate=2025-09-29"
)

resp = requests.get(url)
data = resp.json()

# Example: list dates and matchups
for date in data.get("dates", []):
    print(date["date"])
    for game in date["games"]:
        away = game["teams"]["away"]["team"]["name"]
        home = game["teams"]["home"]["team"]["name"]
        print(f"  {away} at {home}")