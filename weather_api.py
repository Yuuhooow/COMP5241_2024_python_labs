import streamlit as st
import json
import requests
import pandas as pd

# Fetch the weather data
response = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
result_dict = response.json()

# Create a DataFrame from the JSON data
data = result_dict["temperature"]["data"]
df = pd.DataFrame(data)

# Display a bar chart of temperatures for all locations
st.bar_chart(df.set_index("place")["value"])

# Add a sidebar with a dropdown for selecting a location
location = st.sidebar.selectbox("选择一个地点", df["place"])

# Display the temperature for the selected location
selected_temp = df[df["place"] == location]["value"].values[0]
st.write(f"{location} 的温度是 {selected_temp}°C")