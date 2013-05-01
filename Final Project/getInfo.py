from collections import defaultdict
import json
import sys

def Get_Info( user_info ):
    career_count = defaultdict(int)
    career_probability = defaultdict(float)
    total_played = 0

    for user in user_info:
        time_played = user_info[user]
        for career in time_played:
            if time_played[career] != 0.0:
                career_count[career] += 1
                total_played += 1
                
    for career in career_count:
        career_probability[career] = 1.0 * career_count[career] / total_played

    return career_probability


def main():
    user_info = defaultdict()
    with open( "userDict.json", "r" ) as f:
        for record in f.readlines():
            record = json.loads( record )
            if record[0].has_key("battleTag"):
                user_info[ record[0]["battleTag"] ] = record[0]["timePlayed"]
    career_probability = Get_Info( user_info )        

    with open( "careerProbability.json", "w" ) as g:
        g.write( json.dumps(career_probability) + "\n" )

    with open( "timePlayed.json", "w" ) as h:
        h.write( json.dumps(user_info) + "\n" )


if __name__ == "__main__":
    main()
