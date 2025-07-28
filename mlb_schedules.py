import requests, time
import pandas as pd
from bs4 import BeautifulSoup

base_url = "https://www.baseball-reference.com/"
schedule_url = "https://www.baseball-reference.com/leagues/MLB-schedule.shtml"

response = requests.get(schedule_url)
soup = BeautifulSoup(response.text, 'html.parser')
