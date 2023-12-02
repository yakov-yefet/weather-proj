
import streamlit as st
import yaakov_weather_api as yw
import pandas as pd

# Title for your app
st.title("Yaakov's Weather Project")

# local time
# ist_time = yw.get_date_time()
# st.write(f"Israel time: {ist_time}")
st.subheader(yw.preprint_date_time())
st.code(yw.preprint_temperature_of_city())

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
st.code(yw.preprint_temperature_of_city(selected_value))

# table
on = st.toggle(f"Show weather details of ***{selected_value}***")

if on:
    df = pd.DataFrame(yw.preprint_weather_of_city(selected_value))
    df






