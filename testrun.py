from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle 
from datetime import datetime, timedelta


def create_calendar(name):
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)

    credentials = flow.run_console()

    pickle.dump(credentials, open("token.pkl", "wb"))
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)

    result = service.calendarList().list().execute()

    start_time = datetime(2022, 8, 7, 21, 0, 0)
    end_time = start_time + timedelta(hours=2)

    timezone = 'America/New_York'

    name = name

    event = {
      'summary': name,
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()