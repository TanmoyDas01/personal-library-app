import gspread
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "tanmoys_library"


@st.cache_resource
def connect_sheet():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Load credentials from Streamlit Secrets
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"],
    scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1

    return sheet


@st.cache_data(ttl=60)
def load_books():

    sheet = connect_sheet()

    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    return df