import pyttsx3
import json
import requests

def weather_app():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Setting the speech speed
    engine.setProperty('volume', 1.0)  # Setting the volume level (1.0 is maximum)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index for male/female voice

    # Welcome speech
    welcome_text = "Welcome to the Weather App Created by Manish Choudhary. Please enter a city name."
    print(welcome_text)
    engine.say(welcome_text)
    engine.runAndWait()

    while True:
        city = input("\nEnter the City (or type 'exit' to quit): ")

        if city.lower() == 'exit':
            print("Exiting Weather App... Goodbye!")
            engine.say("Exiting Weather App... Goodbye!")
            engine.runAndWait()
            break

        engine.say(f"Fetching weather details for {city}")
        engine.runAndWait()

        try:
            url = f"https://api.weatherapi.com/v1/current.json?key=3fdfded647724b24b06160353251103&q={city}"
            response = requests.get(url)
            data = response.json()

            # Check if the city is invalid
            if "error" in data or "location" not in data:
                print("❌ Invalid city name! Please try again.")
                engine.say("Invalid city name! Please try again.")
                engine.runAndWait()
                continue

            temp_c = data["current"]["temp_c"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]

            weather_text = (
                f"\nWeather in {city}:\n"
                f"🌡 Temperature: {temp_c}°C\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬 Wind Speed: {wind_speed} km/h\n"
            )

            print(weather_text)
            engine.say(f"The current temperature in {city} is {temp_c} degrees Celsius. "
                       f"Humidity is {humidity} percent, and the wind speed is {wind_speed} kilometers per hour.")
            engine.runAndWait()

        except Exception as e:
            print("Error fetching weather data. Please check your internet connection.")
            engine.say("Error fetching weather data. Please check your internet connection.")
            engine.runAndWait()

if __name__ == "__main__":
    weather_app()
