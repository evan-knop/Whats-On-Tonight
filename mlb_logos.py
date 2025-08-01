from db import get_all_teams, get_team_by_id

##TODO: Import MLB Teams Data to get team IDs. Then loop through the teams and get their logos.
'https://www.mlbstatic.com/team-logos/team-cap-on-dark/158.svg'


# Get all teams as a DataFrame
teams_df = get_all_teams()

team_id_list = teams_df['team_id'].tolist()

# Loop through teams and using ID, get the team's logos
for team in team_id_list:
    team_id = int(team)  # Ensure team_id is an integer
    team_name = teams_df.loc[teams_df['team_id'] == team_id, 'team_name'].values[0]
    logo_url = f"https://www.mlbstatic.com/team-logos/team-cap-on-dark/{team_id}.svg"
    
    # Here you would typically download the logo or process it further
    print(f"Team ID: {team_id}, Team: {team_name}, Logo URL: {logo_url}")