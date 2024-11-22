# Terminal-Based Weather API

This project implements a simple terminal-based application that fetches and displays weather information using the RapidAPI OpenWeather API.  The application continuously updates the weather data and displays it in a user-friendly format.

## Features

* Fetches weather data for London, UK (currently hardcoded, but easily modifiable).
* Displays current temperature, feels like temperature, humidity, and weather conditions.
* Uses environment variables to securely store the RapidAPI key.
* Includes comprehensive error handling for API requests and data parsing.
* Clears the terminal before each update for better readability.
* Uses formatted output for a clean and organized display.
* Continuous updates until manually interrupted (Ctrl+C).

## Requirements

* Python 3.7+
* `requests` library:  Install using `pip install requests`

## Setup

1. **Obtain a RapidAPI Key:** Sign up for a free account at [RapidAPI](https://rapidapi.com/) and obtain an API key for the OpenWeatherMap API.

2. **Set Environment Variable:** Set the `RAPIDAPI_KEY` environment variable with your API key.  How you do this depends on your operating system:

   * **Linux/macOS:** `export RAPIDAPI_KEY="your_api_key"`
   * **Windows:** `set RAPIDAPI_KEY="your_api_key"`

3. **Clone the Repository:** Clone this repository to your local machine.

4. **Run the Application:** Execute the `weather_terminal.py` script using `python weather_terminal.py`.

## Usage

The application will start fetching and displaying weather data.  Press `Ctrl+C` to exit.

## Code Structure

The code is organized into a single Python file (`weather_terminal.py`) containing the `WeatherAPI` class.  This class handles:

* API key management
* API requests
* Data parsing
* Terminal display

The `main` function creates an instance of `WeatherAPI` and runs the main loop.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License](LICENSE)
