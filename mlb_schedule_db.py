import pandas as pd
import sqlite3

df = pd.read_csv("mlb_schedule.csv")

#Create a SQLite database connection
conn = sqlite3.connect("mlb_schedule.db")

# Write the DataFrame to a SQLite table
df.to_sql("teams", conn, if_exists="replace", index=False)
print("Saved mlb_schedule.db")

conn.close()