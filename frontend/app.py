import streamlit as st
import pandas as pd

st.title("What's Worth Watching - MLB")
df = pd.read_csv("mlb_schedule.csv")
st.dataframe(df)
