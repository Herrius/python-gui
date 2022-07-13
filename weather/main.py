import requests,datetime
import config
weather_api='http://api.weatherapi.com/v1/forecast.json?'

weather_params={
    "q":[-12.07,-75.23],
    "days":2,
    "key":config.api_key,
}
data_rain=[]
response=requests.get(weather_api,params=weather_params)
data=response.json()
latitud=data["location"]["lat"]
longitud=data["location"]["lon"]
print(latitud,longitud)
print(f"Status code: {response}")
print(f"Status code: {response.status_code}")
weather_hour=data["forecast"]["forecastday"]

time_now=datetime.datetime.now()
hour_now=time_now.hour
day_now=time_now.day
date_now=f"{day_now} {hour_now}"
for date in weather_hour:
    for hour in date["hour"]:
        hours=hour["time"]
        rain_hour={
            "day":hour["time"],
            "raining":hour["chance_of_rain"]
        }
        data_rain.append(rain_hour)
for rain in data_rain:

    day_hour=rain["day"]
    splitter=slice(8,13)
    date_future=day_hour[splitter]
    if date_future==date_now and rain["raining"]>50:
        print("Take a umbrella")

