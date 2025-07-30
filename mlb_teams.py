import requests, pandas as pd

url = (
    "https://statsapi.mlb.com/api/v1/teams"
    "?sportId=1"
)

#Fetch Data
resp = requests.get(url)
data = resp.json()

teams_csv = "mlb_teams.csv"
teams = []

for team in data.get("teams"):
    team_id = team.get("id")
    abbreviation = team.get("abbreviation")
    team_name = team.get("name")
    league_id = team.get("league", {}).get("id") # Get league if it exists, then get nested id
    league_name = team.get("league", {}).get("name")
    division_id = team.get("division", {}).get("id")
    division_name = team.get("division", {}).get("name")

    row = {
            "team_id": team_id,
            "abbreviation": abbreviation,
            "team_name": team_name,
            "league_id": league_id,
            "league_name": league_name,
            "division_id": division_id,
            "division_name": division_name
        }
    
    teams.append(row)

# Load to DataFrame and save
df = pd.DataFrame(teams)
df.to_csv(teams_csv, index=False)

print("Saved mlb_teams.csv")