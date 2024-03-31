# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

#url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
#url = "https://docs.google.com/spreadsheets/d/1kB0oWRD6vOnNHzilJdofS6AF1u-hBTHYPP-ELi0GADo/edit#gid=258115823"
url = "https://docs.google.com/spreadsheets/d/1kB0oWRD6vOnNHzilJdofS6AF1u-hBTHYPP-ELi0GADo/edit?usp=sharing"

#conn = st.experimental_connection("gsheets", type=GSheetsConnection)
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url,worksheet="258115823")
st.dataframe(data)
