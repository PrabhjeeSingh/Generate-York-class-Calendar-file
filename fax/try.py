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

points={}
ranks=[]
def update_rank(points):
    for k,v in points.items():

        return
# Output [{"team":"name","win":2,"losses":1}, {...}, ...]

result ={}

for match in games:
    home = match.get("home_team")
    away = match.get("away_team")
    winner = match.get("winning_team")


    if home not in result:
        result[home]={"win":0,"loses":0,"tie":0,"points":0}
        
    
    if away not in result:
        result[away]={"win":0,"loses":0,"tie":0,"points":0}
    
    if (home == winner):
        result[home]["win"]+=1
        result[away]["loses"]+=1
        result[home]["points"]+=3
        result[away]["points"]-=1

    elif(away==winner):
        result[away]["win"]+=1
        result[home]["loses"]+=1
        result[away]["points"]+=1
        result[home]["points"]+=1

    else:
        result[away]["tie"]=+1
        result[home]["tie"]=+1
        result[away]["points"]=+1
        result[home]["points"]=+1
        print(f"Home: {home} away: {away} win : {winner}")

    update_rank()
   

final=[]

for k,v in result.items():
    final.append({"team":k, "wins":v["win"],"loses":v["loses"],"ties":v["tie"], "points":v["points"]})
    
ranks= sorted(final,key=lambda x:x["points"],reverse =True)
print(json.dumps(ranks))
# print(json.dumps(sorted(final,key= lambda x:x["wins"],reverse=True)))
