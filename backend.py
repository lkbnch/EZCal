import sqlite3
from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle 
from datetime import datetime, timedelta
from testrun import create_calendar

# connect to database
conn = None
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

rows = cursor.execute("SELECT id, title, complete FROM todo").fetchall()

# print(create_calendar('hi'))
print(rows)
for x in rows:
    print(x[1])
    create_calendar(x[1])





def split_event():
    # split event into work blocks + 5 min breaks
    pass

conn.close()