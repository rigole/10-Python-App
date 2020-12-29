import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower() #to check cqse because the json file doesn't capital letters
    if w in data:
       return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, get_close_matches(w, data.keys()))[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This word doesn't exist. Please Check it"
        else:
            return "This word is not in the dictionnary "
    else:
        return "The word doesn't exist. Please Check-it"

word = input("Entrer the word :")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)