import gspread
import pandas as pd
import streamlit as st
import json
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "tanmoys_library"

@st.cache_resource
def connect_sheet():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds_dict = json.loads(st.secrets["gcp_service_account"]["credentials"])

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        creds_dict,
        scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1

    return sheet