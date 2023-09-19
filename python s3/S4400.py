# Kopier mappen 30_danskcargo\milestones\90_api+unittest\ og dens indhold i din løsnings-repository
#
# Kig på 90_api+unittest\weather.py
# Find ud af, hvad programmet gør. Til dette formål:
#     - læs https://www.w3schools.com/python/ref_requests_get.asp
#     - læs https://www.w3schools.com/python/python_json.asp
#     - benyt debugger'en
#
# Kopier værdien af variablen "url" ind i din webbrowsers adresslinje.
# Kopier resultatet fra browservinduet i en JSON-editor.
# Benyt fx https://jsoneditoronline.org/
# Leg med weather.py. Få programmet til at vise nogle andre værdier man kan hente via API'en.
#
#
#

import json
import requests


weather_translation = {
    "Clear": "Klart ⛱",
    "Clouds": "Overskyet ☁",
    "Drizzle": "Støv regn ",
    "Rain": "Rejnvejr ☔",
    "Snow": "Snevejr ☃",
}


def translate_weather_description(english_description):
    return weather_translation.get(english_description, english_description)


KEY = "2a3891ce1248786a1398a888debb0368"  # ulsc@aspit.dk


def weather_now(city, key=KEY):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + key
    # print(url)
    response = requests.get(url)  # Some background information: https://www.w3schools.com/python/ref_requests_get.asp
    weather = json.loads(response.text)  # https://www.w3schools.com/python/python_json.asp  Deserialize json into a hierarchy of dictionaries and lists
    # print(f'{weather=}')
    # print(f'{weather["weather"]=}')
    # print(f'{weather["weather"][0]["main"]=}')
    # print(f'{int(weather["main"]["temp"])=}')
    if weather["cod"] == 404:
        return "Kunne ikke finde nogle værdier der matcher!"
    elif weather["cod"] == 200:
        english_description = weather["weather"][0]["main"]
        danish_description = translate_weather_description(english_description)
        weather_report = danish_description + ", " + str(int(weather["main"]["temp"])) + "°C"
        return weather_report
    else:
        return f'Kunne ikke finde en by ved navn: {city}.'


if __name__ == "__main__":  # Executed when invoked directly
    while True:
        city = str(input("By Navn: "))
        if str.lower(city) in ["slut", "exit", "færdig", "bli", "ferdig", "bli ferdig", "stop", "stoppe"]:
            exit()
        print(weather_now(city, KEY))
    # print(weather_now("xxxxzzzyy", KEY))
