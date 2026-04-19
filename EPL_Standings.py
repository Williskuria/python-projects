import requests

response = requests.get(
    "https://api.football-data.org/v4/competitions/PL/standings",
    headers={"X-Auth-Token": "8ed0b244bb844f2b8a816e6a98403f54"},
    verify=False
)
data = response.json()

table = data["standings"][0]["table"]    

for team in table:
    position = team["position"]
    name = team["team"]["name"]
    points = team["points"]
    played = team["playedGames"]
    print(f"{position}.{name} - {points} pts({played}games)")














"""for team in table:
    position = team["position"]
    name = team["team"]["name"]
    points = team["points"]
    played = team["playedGames"]
    print(f"{position}.{name} - {points} pts({played}games)")"""

