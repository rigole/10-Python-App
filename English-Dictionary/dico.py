import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower() #to check cqse because the json file doesn't capital letters
    if w in data:
       return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, get_close_matches(w, data.keys()))[0]
    else:
        return "The word doesn't exist. Please Check-it"

word = input("Entrer the word :")

print(translate(word))