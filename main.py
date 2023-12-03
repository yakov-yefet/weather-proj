import streamlit as st
import yaakov_weather_api as yw
import pandas as pd

# Title for your app
st.title("BIU DS16 - Python Project 1 - Weather Forecast")
st.header('Local Time & Temp')

# local time
st.subheader(yw.preprint_date_time())
local_temp_text, local_temp_icon = yw.preprint_temperature_of_city()

# set text and icon on the same line
col1, col2 = st.columns([1, 7])
with col1:
    st.image(local_temp_icon, width=50)
with col2:
    st.code(local_temp_text)

st.markdown("---")
st.header('Remote Time & Temp')
# Dictionary with key-value pairs
options_dict = {
    "Asia/Jerusalem": "Jerusalem",
    "Europe/Berlin": "Berlin",
    "Asia/Kolkata": "Kolkata",
    "Australia/Sydney": "Sydney"
}

# Create the select box using dictionary values
selected_value = st.selectbox("Choose a city:", options_dict.values())

# Find the key that corresponds to the selected value
selected_key = yw.get_key(selected_value, options_dict)

# print to screen
st.subheader(yw.preprint_date_time(selected_key, selected_value))
selected_temp_text, selected_temp_icon = yw.preprint_temperature_of_city(selected_value)
# set text and icon on the same line
col3, col4 = st.columns([1, 7])
with col3:
    st.image(selected_temp_icon, width=50)
with col4:
    st.code(selected_temp_text)

# table
on = st.toggle(f"Show weather details of ***{selected_value}***")

if on:
    df = pd.DataFrame(yw.preprint_weather_of_city(selected_value))
    df
