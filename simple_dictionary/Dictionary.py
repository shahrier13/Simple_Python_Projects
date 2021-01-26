import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" % get_close_matches(word, data.keys())[0])
        decide = input("press Y for yes or N for no: ")
        decide = decide.lower()
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("  not found  ")
        else:
            return("You have pressed wrong key! please enter Y or N: ")
    else:
        return "  not found  "

while True:
    word = input("Enter your Word: ")
    translation = translate(word)

    if type(translation) == list:
        print(f"{word} means: ")
        for i in translation:
            print(i)
    else:
        print(f"{word} means : {translation}")
    print()
    print("................ ...................")
    print()
    next = input("For search more press Y. To exit press X: ")
    next = next.upper()
    if next == "Y":
        print()
        print("............... x .................")
        print()
        continue

    else:
        print()
        print("............... x .................")
        print()
        break



