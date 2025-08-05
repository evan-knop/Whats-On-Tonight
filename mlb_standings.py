import requests, pandas as pd

url = "https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season=2025&standingsTypes=regularSeason"


#Fetch Data
resp = requests.get(url)
data = resp.json()

standings_csv = "mlb_standings.csv"
standings = []

for row in data.get("records", []):
    row.get("teamRecords", [])
    for team in row.get("teamRecords", []):
        team_id = team.get("team", {}).get("id")
        team_name = team.get("team", {}).get("name")
        wins = team.get("wins")
        losses = team.get("losses")
        win_percentage = team.get("winPercentage")
        games_back = team.get("gamesBack")
        division_rank = team.get("divisionRank")
        wild_card_rank = team.get("wildCardRank")

        row_data = {
            "team_id": team_id,
            "team_name": team_name,
            "wins": wins,
            "losses": losses,
            "win_percentage": win_percentage,
            "games_back": games_back,
            "division_rank": division_rank,
            "wild_card_rank": wild_card_rank
        }
        
        standings.append(row_data)

df = pd.DataFrame(standings)
df.to_csv(standings_csv, index=False)
print(f"Saved {len(standings)} teams to {standings_csv}")