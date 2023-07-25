import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

def get_weather_data(date):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    weather_data = data["list"][0]["main"]
    return {
        "date": date,
        "temperature": weather_data["temp"],
        "description": data["list"][0]["weather"][0]["description"],
    }


def get_wind_speed_data(date):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
  
    wind_data = data["list"][0]["wind"]
    return {
        "date": date,
        "wind_speed": wind_data["speed"],
    }


def get_pressure_data(date):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    pressure_data = data["list"][0]["main"]["pressure"]
    return {
        "date": date,
        "pressure": pressure_data,
    }


def get_user_choice():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    return int(input("Enter your choice: "))


def get_user_date():
    return input("Enter the date (YYYY-MM-DD): ")


def main():
    while True:
        choice = get_user_choice()

        if choice == 1:
            date = get_user_date()
            weather_data = get_weather_data(date)
            print(f"Weather on {weather_data['date']}: {weather_data['temperature']}°C, {weather_data['description']}")

        elif choice == 2:
            date = get_user_date()
            wind_data = get_wind_speed_data(date)
            print(f"Wind Speed on {wind_data['date']}: {wind_data['wind_speed']} km/h")

        elif choice == 3:
            date = get_user_date()
            pressure_data = get_pressure_data(date)
            print(f"Pressure on {pressure_data['date']}: {pressure_data['pressure']} hPa")

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
