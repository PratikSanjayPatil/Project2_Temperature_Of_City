import requests

def measure_temperature(Api_key, City_name):
    Data_Source = "http://api.openweathermap.org/data/2.5/weather"
    Dict = {
        "q": City_name,
        "appid": Api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(Data_Source, params=Dict)
                    
        data = response.json()
        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            return temperature
        else:
            print("City Not Found!")
    except Exception:
        print("Error")


Api_key = "c715584911935689fc7a3e5e9122fc16"
while(True):
    Choose = int(input("Enter 1 for measure Temperature otherwise press 0: "))
    if(Choose == 1):
        City_name = input("Enter the name of the city: ")

        temperature = measure_temperature(Api_key, City_name)
        if temperature is not None:
            print(f"The current temperature in {City_name} is {temperature}°C.")
    else:
        print("Thank You!") 
        break       
