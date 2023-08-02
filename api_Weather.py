import requests 

city_input = input("Enter Your City Name: ")

api_key = "2e80c3da5cae1a7b31a2d88f5169de50"

def get_weather(api_key,city_input):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}"

    url_response = requests.get(url).json()


    temperature = url_response["main"]["temp"]
    
    temp_old = (temperature )-273.15 # coverts to C
    temp = format(temp_old,".2f") 
    
    print("The temperature in",city_input,"is",str(temp)+"°C")
    

get_weather(api_key, city_input)

# Hi My name is Sumit i am cap 04 batch. and my project is -  Using API to fetch the weather ☁️🌡️ of the city 

#made with ❤️ by Sumit


# Name = Sumit Kumar
# Batch = Cap04
# cap_id = cap04_075