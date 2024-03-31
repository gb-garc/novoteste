import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1GswNpQuhhc6udp59clV5s6dDnBfFF91rofaRbMsDdT0/edit#gid=704841034"

@st.cache(allow_output_mutation=True)
def get_gsheets_connection():
    return GSheetsConnection()

conn = get_gsheets_connection()
df = conn.read(spreadsheet=url, worksheet="METRICAS", usecols=list(range(15)))
st.dataframe(df)


#import streamlit as st
#from streamlit_gsheets import GSheetsConnection
#url = "https://docs.google.com/spreadsheets/d/1GswNpQuhhc6udp59clV5s6dDnBfFF91rofaRbMsDdT0/edit#gid=704841034"
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
