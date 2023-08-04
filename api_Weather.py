import requests

api_key = "2e80c3da5cae1a7b31a2d88f5169de50"

def get_weather(api_key, city_input):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}"

    try:
        url_response = requests.get(url).json()

        if url_response.get("cod") == 200: # checks the if the response "cod" with value of 200 # https 
            temperature = url_response["main"]["temp"]
            temp_celsius = temperature - 273.15 # converts to c
            temp = format(temp_celsius, ".2f")
            print("The temperature in", city_input, "is", str(temp) + "°C")
            return True
        else:
            print("Error: Invalid city name or failed in data fetching.")
            return False
    except requests.exceptions.RequestException as error:
        print("Error: An error occurred while making the request.")
        print(error)
        return False

while True: # extra from my side if user puts a wrong city name then again it will ask you to enter your city name
    city_input = input("Enter Your City Name: ")
    getweather = get_weather(api_key, city_input)
    if getweather == True:
        break

# Hi My name is Sumit i am cap 04 batch. and my project is -  Using API to fetch the weather ☁️🌡️ of the city 

#made with ❤️ by Sumit


# Name = Sumit Kumar
# Batch = Cap04
# cap_id = cap04_075
