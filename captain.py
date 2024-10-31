import json

with open('matches.json', 'r') as file:
    data = json.load(file)

def find_beer(food):
    out = []
    for pairing in data["pairings"]:
        for dish in pairing["matches"]:
            if food.lower() in dish["dish"].lower():
                out.append({"beer": pairing["beer"], "score": dish["match_percentage"]})
    return out

def find_food(beer):
    out = []
    for pairing in data["pairings"]:
        if beer.lower() in pairing["beer"].lower():
            out = [(match["dish"], match["match_percentage"]) for match in pairing["matches"]]
    return out

def get_food():
    out = []
    for pairing in data["pairings"]:
        for entry in pairing["matches"]:
            [out.append(entry["dish"]) if entry["dish"] not in out else None]
    return out

def get_beers():
    out = []
    for pairing in data["pairings"]:
        out.append(pairing["beer"])
    return out