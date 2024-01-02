import json
games = [
  { "home_team": "Raptors", "away_team": "Cavaliers", "winning_team": "Cavaliers" },
  { "home_team": "Cavaliers", "away_team": "Celtics", "winning_team": "Cavaliers" },
  { "home_team": "Celtics", "away_team": "Lakers", "winning_team": "Celtics" },
  { "home_team": "Cavaliers", "away_team": "Lakers", "winning_team": "Cavaliers" },
  { "home_team": "Celtics", "away_team": "Raptors", "winning_team": "Raptors" },
  { "home_team": "Lakers", "away_team": "Raptors", "winning_team": "Raptors" },
  { "home_team": "Celtics", "away_team": "Cavaliers", "winning_team": "Celtics" }
]

#We expect you to produce an output of standings records in the following JSON format:
#
#[
#  { "team": "Raptors", "wins": 2, "losses": 1 },
#  { "team": "Cavaliers", ... },
#  { ... }
#]
# {Raptors :[0,0]}
# result={home: {win:0,los:0}}
result={}


for i in games:
    home = i.get("home_team")
    away = i.get("away_team")
    wining= i.get("wining_team")


    if home not in result:
        result[home]= {"win":0,"lose":0}
    if away not in result:
        result[away]= {"win":0,"lose":0}
 

    if (home==wining):
        result[home]["win"]+=1
        result[away]["lose"]+=1
      
    else:
        result[away]["win"] +=1
        result[home]["lose"] +=1

final=[]
for k,v in result.items():
    final.append({"team":k,"wins":v["win"],"loses":v["lose"]})

sorted = sorted(final,key= lambda x: x["wins"])
print(json.dumps(sorted))
