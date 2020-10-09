import json
import urllib3


def lambda_handler(event, context):
    city = event["currentIntent"]["slots"]["City"]
    endpoint = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"q": city, "appid": " COPY YOUR KEY HERE "}

    http = urllib3.PoolManager()
    r = http.request('GET', endpoint, fields=parameters)
    data = json.loads(r.data.decode('utf8'))

    weather_main = data['weather'][0]['main']
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']

    reply = f"The weather in {city} is {weather_main}. Temperature is : {temp} Pressure is : {pressure} and Humidity is: {humidity}"
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                    "contentType": "PlainText",
                    "content": reply
            }
        }
    }
