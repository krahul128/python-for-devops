import requests

url = "https://official-joke-api.appspot.com/random_joke"

# this code is for practice purpose only to import API reques

def get_jokes():
    
    response = requests.get(url=url)
    for item,value in response.json().items():
        if item == "setup" or item == "punchline":
            print(item,value)

get_jokes()