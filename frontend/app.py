import streamlit as st
import pandas as pd
import sqlite3

def load_joined_data():
    conn = sqlite3.connect("data.db")
    
    query = """
    SELECT 
        home_teams.team_name AS home_team,
        home_teams.logo_url AS home_logo,
        away_teams.logo_url AS away_logo,
        away_teams.team_name AS away_team,
        s.date
    FROM schedule s
    JOIN teams home_teams ON s.home = home_teams.team_name
    JOIN teams away_teams ON s.away = away_teams.team_name    
    WHERE s.date >= date('now')
    AND s.date <= date('now', '+7 days')
    ORDER BY s.date
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.title("What's Worth Watching - MLB")
df = load_joined_data()

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
                <div style='text-align: center; font-weight: bold; margin-bottom: 5px;'>{row['date']}</div>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div style='text-align: center; width: 40%;'>
                        <img src="{home_logo}" style="width:40px; max-height:40px; object-fit: contain;"/><br/>
                        {row['home_team']}
                    </div>
                    <div style='font-size: 18px; font-weight: bold;'>vs</div>
                    <div style='text-align: center; width: 40%;'>
                        <img src="{away_logo}" style="width:40px; max-height:40px; object-fit: contain;"/><br/>
                        {row['away_team']}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    # Reset columns every `num_cols`
    if (idx + 1) % num_cols == 0 and (idx + 1) < len(df):
        cols = st.columns(num_cols)
