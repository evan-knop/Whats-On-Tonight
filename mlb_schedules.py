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

schedule_csv = "mlb_schedule.csv"
games = []

# Collect all games data
for date in data.get("dates", []):
    game_date = date["date"]
    for game in date["games"]:
        away = game["teams"]["away"]["team"]["name"]
        home = game["teams"]["home"]["team"]["name"]
        
        row = {
            "date": game_date,
            "home": home,
            "away": away
        }
        
        games.append(row)

# Load to DataFrame and save
df = pd.DataFrame(games)
df.to_csv(schedule_csv, index=False)

print(f"Saved {len(games)} games to {schedule_csv}")