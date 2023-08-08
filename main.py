import requests as re

public_api_url = "https://zsr.octane.gg/"

def call_api(category, options):
    response = re.get(public_api_url + category, options)
    return response.json()

worlds_events = call_api("events", {"name":"World Championship", "tier":"S"})
teams = {}
for element in worlds_events['events']:
    print(str(element["_id"]))
    event_team = call_api("events/"+ str(element["_id"]) + "/participants", "")
    for element in event_team['participants']:
        if element['team']['_id'] not in teams['_id']:
            teams[element['team']['_id']] = 1