blazers_games = [
    {
        "blazers": 108,
        "opponent": "Nuggets",
        "opponent_score": 140
    },
    {
        "blazers": 114,
        "opponent": "Nets",
        "opponent_score": 108 
    },
    {
        "blazers": 103,
        "opponent": "Kings",
        "opponent_score": 88
    },
    {
        "blazers": 101,
        "opponent": "cavaliers",
        "opponent_score": 114
    },
]

total_score = list(map(lambda x: x.get("blazers") + x.get("opponent_score"), blazers_games))
print('Total Score', total_score)

blow_out = list(filter(lambda x: x.get("opponent_score") > 110, blazers_games))
print("Blow out losses", blow_out)