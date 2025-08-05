import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime


def load_joined_data():
    conn = sqlite3.connect("data.db")
    
    query = """
    SELECT 
        home_teams.team_name AS home_team,
        home_teams.logo_url AS home_logo,
        home_standings.wins AS home_wins,
        home_standings.losses AS home_losses,
        
        away_teams.team_name AS away_team,
        away_teams.logo_url AS away_logo,
        away_standings.wins AS away_wins,
        away_standings.losses AS away_losses,
        s.date
    FROM schedule s
    JOIN teams home_teams ON s.home = home_teams.team_name
    JOIN teams away_teams ON s.away = away_teams.team_name

    LEFT JOIN standings home_standings ON home_teams.team_id = home_standings.team_id
    LEFT JOIN standings away_standings ON away_teams.team_id = away_standings.team_id

    WHERE s.date >= date('now')
    AND s.date <= date('now', '+7 days')
    ORDER BY s.date
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.title("What's Worth Watching? - MLB")

# Get today's date (formatted however you like)
today = datetime.today().strftime("%B %d, %Y")  # e.g., "August 04, 2025"

df = load_joined_data()

df["home_record"] = df["home_wins"].astype(str) + "-" + df["home_losses"].astype(str)
df["away_record"] = df["away_wins"].astype(str) + "-" + df["away_losses"].astype(str)

num_cols = 2
cols = st.columns(num_cols)
default_logo = "https://via.placeholder.com/40?text=🧩"


for idx, row in df.iterrows():
    col = cols[idx % num_cols]

    home_logo = row["home_logo"] if row["home_logo"] else default_logo
    away_logo = row["away_logo"] if row["away_logo"] else default_logo

    with col:
        st.markdown(
            f"""
            <div style='border: 1px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 10px;'>
                <div style='text-align: center; font-weight: bold; margin-bottom: 10px;'>{row['date']}</div>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div style='display: flex; flex-direction: column; align-items: center; width: 40%; min-height: 100px;'>
                        <img src="{home_logo}" style="width:40px; max-height:40px; object-fit: contain; margin-bottom: 5px;"/>
                        <div style="font-weight: bold; text-align: center; max-width: 100px;">
                            {row['home_team']}
                        </div>
                        <div style="font-size: 12px; color: #555;">{row['home_record']}</div>
                    </div>
                    <div style='font-size: 18px; font-weight: bold;'>vs</div>
                    <div style='display: flex; flex-direction: column; align-items: center; width: 40%; min-height: 100px;'>
                        <img src="{away_logo}" style="width:40px; max-height:40px; object-fit: contain; margin-bottom: 5px;"/>
                        <div style="font-weight: bold; text-align: center; max-width: 100px;">
                            {row['away_team']}
                        </div>
                        <div style="font-size: 12px; color: #555;">{row['away_record']}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

                
    # Reset columns every `num_cols`
    if (idx + 1) % num_cols == 0 and (idx + 1) < len(df):
        cols = st.columns(num_cols)
