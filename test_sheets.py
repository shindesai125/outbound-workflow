import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Load environment variables
load_dotenv()

# Get values from .env
SHEET_ID = os.getenv("GOOGLE_SHEETS_ID")
SA_PATH = os.getenv("GOOGLE_SA_JSON")

# Authenticate
creds = Credentials.from_service_account_file(
    SA_PATH,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

# Build Sheets API client
service = build("sheets", "v4", credentials=creds)

# Prepare test data
body = {
    "values": [["Hello from Sai", "✅ Test row written successfully"]]
}

# Append to the sheet
result = service.spreadsheets().values().append(
    spreadsheetId=SHEET_ID,
    range="Sheet1!A1",  # Change this if your tab name is different
    valueInputOption="RAW",
    body=body
).execute()

print("✅ Append result:", result)