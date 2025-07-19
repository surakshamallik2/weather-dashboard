import streamlit as st
import requests
import pandas as pd

# ---------------------
# Page Config
# ---------------------
st.set_page_config(page_title="🌦️ Weather Dashboard", layout="wide")

# ---------------------
# Title
# ---------------------
st.markdown("<h1 style='text-align: center; color: #3366cc;'>🌍 Weather Dashboard</h1>", unsafe_allow_html=True)
st.markdown("##")

# ---------------------
# Input Section
# ---------------------
city = st.text_input("Enter City Name", "Bangalore")

# ---------------------
# Fetch Weather Data
# ---------------------
api_key = st.secrets["api"]["weather_api"]  # Replace with your OpenWeatherMap API key

def get_weather(city_name):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

data = get_weather(city)

# ---------------------
# Display Data
# ---------------------
if data:
    st.success(f"Showing weather for {data['name']}, {data['sys']['country']}")

    # Layout with columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🌡️ Temperature", value=f"{data['main']['temp']} °C")
    with col2:
        st.metric(label="💧 Humidity", value=f"{data['main']['humidity']}%")
    with col3:
        st.metric(label="🌬️ Wind Speed", value=f"{data['wind']['speed']} m/s")

    # Weather description
    st.markdown(f"**Condition:** {data['weather'][0]['main']} - {data['weather'][0]['description'].capitalize()}")

    # ---------------------
    # Map Location
    # ---------------------
    lat = data['coord']['lat']
    lon = data['coord']['lon']

    st.markdown("### 🗺️ Location on Map")
    df_map = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(df_map, zoom=8)

else:
    st.error("City not found or API key is invalid. Please try again.")

