import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/1GswNpQuhhc6udp59clV5s6dDnBfFF91rofaRbMsDdT0/edit#gid=704841034"
google_sheets_table = conn.read(spreadsheet=url)
dataframe = pd.DataFrame(google_sheets_table) # Convert google sheets table into python dataframe. Streamlit expects dataframes as input.

#conn = st.connection("gsheets", type=GSheetsConnection)
#df = conn.read(spreadsheet=url, worksheet="METRICAS", usecols=list(range(15)))
#st.dataframe(df)


#url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
#url = "https://docs.google.com/spreadsheets/d/1kB0oWRD6vOnNHzilJdofS6AF1u-hBTHYPP-ELi0GADo/edit#gid=258115823"
#url = "https://docs.google.com/spreadsheets/d/1kB0oWRD6vOnNHzilJdofS6AF1u-hBTHYPP-ELi0GADo/edit?usp=sharing"

#conn = st.experimental_connection("gsheets", type=GSheetsConnection)
#conn = st.connection("gsheets", type=GSheetsConnection)

#data = conn.read(spreadsheet=url, worksheet="METRICAS", usecols=list(range(15)))
#data = conn.read(spreadsheet=url, worksheet="Lista", usecols=list(range(5)))
#st.dataframe(data)
