import json


ifile = open("userDict.json","r")
ofile = open("user-hero.json","w")

dict = {}

for line in ifile:
    tmp = json.loads(line)
    if "battleTag" in tmp[0]:
        if tmp[0]["battleTag"] not in dict:
            dict[tmp[0]["battleTag"]] = tmp[0]["heroes"]

json.dump(dict, ofile)
