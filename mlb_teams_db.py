import pandas as pd
import sqlite3

df = pd.read_csv("mlb_teams.csv")

#Create a SQLite database connection
conn = sqlite3.connect("mlb_teams.db")

# Write the DataFrame to a SQLite table
df.to_sql("teams", conn, if_exists="replace", index=False)
print("Saved mlb_teams.db")

conn.close()