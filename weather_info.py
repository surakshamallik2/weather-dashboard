import requests

def get_weather(city_name, api_key):
    # Base URL
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Full URL with parameters
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        # Extract required information
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city_name.capitalize()}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError:
        print("Error: Could not parse weather data. Please check city name or API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)
