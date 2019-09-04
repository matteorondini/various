import requests
from random import randint
from pyfiglet import figlet_format
from termcolor import colored

print(figlet_format("Jokes API"))
url = "https://icanhazdadjoke.com/search"


def jokes():
    topic = input("Please select the topic of the jokes:")
    response = requests.get(
        url, headers={"Accept": "application/json"}, params={"term": topic}
    )
    data = response.json()
    dictionary = data["results"]
    lendict = len(dictionary)
    if lendict == 1:
        print((dictionary[0]["joke"]), "...I have no more jokes about this topic")
    elif lendict == 0:
        testoerr = colored(
            "No jokes found for your topic ;(", color="red", attrs=["blink"]
        )
        print(testoerr)
    else:
        print(
            (dictionary[randint(0, len(dictionary) - 1)]["joke"]),
            f"...I have {lendict} more jokes about this topic",
        )

jokes()
