import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]

    elif word.lower() in data:
        return data[word.lower()]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys())) >0:
        x=input("Did you meant "%get_close_matches(word,data.keys())[0])
        
    else:
        print("Wrong keys or word Sir")
        return ""

word=input("Enter the word you want to search..\n")
output=translate(word)

for item in output:
    print(item)