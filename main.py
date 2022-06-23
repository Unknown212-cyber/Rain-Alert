import requests
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "cb262911fe8fa20863e84c64b486d117"
account_sid = "AC1ab0949e80201f7e76d1b80e2838b61a"
auth_token = "69f1d502c3d7e1395298900ae1282084"

parameters = {
    "lat": 49.165882,
    "lon": -123.940063,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OMW_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19282856818",
        to="+9180737 54219"
    )

    print(message.status)

# for i in range(12):
#     weather_id = weather_data[i]['weather'][0]['id']
#     if weather_id < 700:
#         print("Bring an Umbrella")
#         break
