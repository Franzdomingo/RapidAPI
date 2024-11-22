import requests
import time
from datetime import datetime
import os
import json
from typing import Dict, Any

class WeatherAPI:
    """A class to fetch and display weather data from RapidAPI's OpenWeather service.
    
    This class handles the API communication, data fetching, and terminal display
    of weather information. It uses the RapidAPI service to get weather data
    for a specified city.
    """

    def __init__(self):
        """Initialize the WeatherAPI with API credentials and endpoint configuration.
        
        The API key should ideally be stored in environment variables for security.
        """
        self.api_key = os.getenv('RAPIDAPI_KEY', "YOUR_API_KEY_HERE")  # API key should be in environment variable
        self.base_url = "https://open-weather13.p.rapidapi.com/city/london/EN"  # Fixed city endpoint
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
        }

    def fetch_weather(self) -> Dict[str, Any]:
        """Fetch weather data from the RapidAPI endpoint.
        
        Returns:
            Dict[str, Any]: Weather data in JSON format, or empty dict if request fails
        
        The method handles HTTP request exceptions and returns an empty dict
        if the request fails.
        """
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return {}

    def display_weather(self, weather_data: Dict[str, Any]) -> None:
        """Display formatted weather information in the terminal.
        
        Args:
            weather_data (Dict[str, Any]): Weather data dictionary from API
            
        The method clears the terminal before displaying new data and handles
        missing or malformed data gracefully.
        """
        if not weather_data:
            print("No weather data available")
            return

        # Clear terminal screen for better visibility
        os.system('cls' if os.name == 'nt' else 'clear')
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("="* 50)
        print(f"Weather Update as of {current_time}")
        print("="* 50)
        
        try:
            # Extract weather data with fallback values if keys don't exist
            temp = weather_data.get('main', {}).get('temp', 'N/A')
            feels_like = weather_data.get('main', {}).get('feels_like', 'N/A')
            humidity = weather_data.get('main', {}).get('humidity', 'N/A')
            description = weather_data.get('weather', [{}])[0].get('description', 'N/A')
            
            print(f"\nTemperature: {temp}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description.capitalize()}")
            
        except (KeyError, IndexError) as e:
            print(f"Error parsing weather data: {e}")
        
        print("="* 50)

def main():
    """Main function to run the weather monitoring application.
    
    Creates a WeatherAPI instance and continuously fetches and displays
    weather data until interrupted by the user.
    """
    weather_api = WeatherAPI()
    
    print("Starting weather monitoring...")
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            weather_data = weather_api.fetch_weather()
            weather_api.display_weather(weather_data)
            time.sleep(1)  # Wait for 1 second before next update
            
    except KeyboardInterrupt:
        print("\nExiting weather monitoring...")

if __name__ == "__main__":
    main() 