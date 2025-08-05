import pandas as pd
import sqlite3

df = pd.read_csv("mlb_standings.csv")

#Create a SQLite database connection
conn = sqlite3.connect("data.db")

# Write the DataFrame to a SQLite table
df.to_sql("standings", conn, if_exists="replace", index=False)
print("Saved standings.db")

conn.close()