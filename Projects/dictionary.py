import json
from difflib import get_close_matches

data = json.load( open("data.json"))
user_input = input("Please enter something to search for : ")
user_input = user_input.lower()

if user_input in data:
        print(data[user_input])

elif len( get_close_matches(user_input,data.keys() ) ) > 0:
        close = get_close_matches(user_input,data.keys() )[0]
        choose = input( "Did you mean,"+close+"? Yes/No \n")
        if choose.lower()=="yes":
            print(data[close])
        else:
            print("Ending Program...")
else:
        print("No value found for your entry.")