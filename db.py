# db.py
import sqlite3
import pandas as pd

def get_connection(db_path="mlb_teams.db"):
    return sqlite3.connect(db_path)

def get_all_teams():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM teams", conn)
    conn.close()
    return df

def get_team_by_id(team_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
    row = cursor.fetchone()
    conn.close()
    return row