import requests
from datetime import datetime
my_long = 78.962883
my_lati = 20.593683
time_now = datetime.now()
parameters = {
    "lat": my_lati,
    "long": my_long,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(time_now.hour)
