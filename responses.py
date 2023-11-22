import random as rd
from strava import get_lunch

greetings = ["Hey!", "Hi there!", "Howdy", "Hello"]
colors = ["Red", "Black", "Green"]



def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "!hello":
        return rd.choice(greetings)
    

    if p_message == "!gamba":
        results = rd.choices(colors, weights = [18, 18, 2], k = 1)
        return str(results)
    

    if p_message == "!help":
        return "`There's no help`"
    
    if p_message == "!lunch":
        return get_lunch()