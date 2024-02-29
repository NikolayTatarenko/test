import json

new_dict = {
    234566: ("Alex", 25),
    343647: ("Jonh", 44),
    557554: ("Anna", 32),
    995735: ("Jack", 22),
    234534: ("Maria", 21),
    4575675: ("Olga", 29)
}

with open("../../data.json", "w") as file:
    json.dump(new_dict, file)

