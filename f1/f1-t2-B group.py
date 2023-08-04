from collections import OrderedDict

teams = {
    "Iran": {
        "wins": 0, "loses" : 0 , "draws" : 0 , "goal difference" : 0 , "points" : 0
    },
    "Spain": {
        "wins": 0, "loses" : 0 , "draws" : 0 , "goal difference" : 0 , "points" : 0
    },
    "Portugal": {
        "wins": 0, "loses" : 0 , "draws" : 0 , "goal difference" : 0 , "points" : 0
    },
    "Morocco": {
        "wins": 0, "loses" : 0 , "draws" : 0 , "goal difference" : 0 , "points" : 0
    }
}
games = [
    ["Iran", "Spain"],
    ["Iran", "Portugal"],
    ["Iran", "Morocco"],
    ["Spain", "Portugal"],
    ["Spain", "Morocco"],
    ["Portugal", "Morocco"],
]
for i in range(0, 6):
    entry = list(map(int, input().split('-')))
    if entry[0] == entry[1]:
        teams[games[i][0]]["draws"] += 1
        teams[games[i][1]]["draws"] += 1

        teams[games[i][0]]["points"] += 1
        teams[games[i][1]]["points"] += 1
    elif entry[0] > entry[1]:
        teams[games[i][0]]["wins"] += 1
        teams[games[i][1]]["loses"] += 1

        teams[games[i][0]]["points"] += 3

        teams[games[i][0]]["goal difference"] += (entry[0] - entry[1])
        teams[games[i][1]]["goal difference"] += (entry[1] - entry[0])
    elif entry[0] < entry[1]:
        teams[games[i][0]]["loses"] += 1
        teams[games[i][1]]["wins"] += 1

        teams[games[i][1]]["points"] += 3
        teams[games[i][1]]["goal difference"] += (entry[1] - entry[0])
        teams[games[i][0]]["goal difference"] += (entry[0] - entry[1])
teams = sorted(teams.items())
teams = sorted(teams, key=lambda t:t[1]["wins"], reverse=True)
teams = sorted(teams, key=lambda t:t[1]["points"], reverse=True)
for i in teams:
    print(i[0], "wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(i[1]["wins"], i[1]["loses"], i[1]["draws"], i[1]["goal difference"], i[1]["points"]))