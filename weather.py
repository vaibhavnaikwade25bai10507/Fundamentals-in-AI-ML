import requests

def get_weather(city_name, api_key):
    # API URL with metric units for Celsius
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extracting data from the JSON response
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            wind = data['wind']['speed']

            print(f"\n--- Current Weather in {city_name.title()} ---")
            print(f"Temperature: {temp}°C")
            print(f"Condition:   {description.capitalize()}")
            print(f"Humidity:    {humidity}%")
            print(f"Wind Speed:  {wind} m/s")
            print("-" * 30)
        else:
            # Displays the specific error from the server (e.g., City Not Found)
            print(f"\nError: {data.get('message', 'Could not retrieve data.')}")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    # Your specific API Key
    MY_API_KEY = '444eb7828a7aa2f78008631c86136049'

    print("Welcome to the Weather Reporter")
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Closing program...")
            break
        
        if city:
            get_weather(city, MY_API_KEY)
        else:
            print("Please enter a valid city name.")
