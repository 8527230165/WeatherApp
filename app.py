import requests
import json
import pyttsx3

city=input("Enter name of the city : ")

url=f"https://api.weatherapi.com/v1/current.json?key=15e942e105c64603b8a65209231306&q={city}"

r=requests.get(url)

print("type(r.text)",type(r.text))

weatherDict=json.loads(r.text)

print(weatherDict["current"]["temp_c"])
weatherinC=weatherDict["current"]["temp_c"]
#print(weatherDict.keys())
#print(weatherDict.values())
voice=f"The Current weather in {city} is "
engine = pyttsx3.init()
engine.say(voice)
for value in weatherDict.values():
    voice=f"{value}"
    engine = pyttsx3.init()
    engine.say(voice)
    engine.runAndWait()
    #print(value)


