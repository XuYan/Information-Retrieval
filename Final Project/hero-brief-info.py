import json


ifile = open("heroDict.json","r")
ofile = open("hero-brief-info.json","w")

dict = {}

for line in ifile:
    tmp = json.loads(line)
    if "id" in tmp[0]:
        if tmp[0]["id"] not in dict:
            dict[tmp[0]["id"]] = {}
            if "name" in tmp[0]:
                dict[tmp[0]["id"]]["name"] = tmp[0]["name"]
            else: dict[tmp[0]["id"]]["name"] = "Unknown"
            
            if "class" in tmp[0]:
                dict[tmp[0]["id"]]["class"] = tmp[0]["class"]
            else: dict[tmp[0]["id"]]["class"] = "Unknown"

            if "level" in tmp[0]:
                dict[tmp[0]["id"]]["level"] = tmp[0]["level"]
            else: dict[tmp[0]["id"]]["level"] = "Unknown"

            if "skills" in tmp[0]:
                dict[tmp[0]["id"]]["skills"] = {}
                dict[tmp[0]["id"]]["skills"]["active"] = []
                dict[tmp[0]["id"]]["skills"]["passive"] = []
                dict[tmp[0]["id"]]["skills"]["rune"] = []

                if "active" in tmp[0]["skills"]:
                    for m in tmp[0]["skills"]["active"]:
                        if "skill" in m:
                            dict[tmp[0]["id"]]["skills"]["active"].append({"name": m["skill"]["name"], "level":m["skill"]["level"]})
                        if "rune" in m:
                            dict[tmp[0]["id"]]["skills"]["rune"].append({"name": m["rune"]["name"], "level":m["rune"]["level"]})
                if "passive" in  tmp[0]["skills"]:
                    for m in tmp[0]["skills"]["passive"]:
                        if "skill" in m:
                            dict[tmp[0]["id"]]["skills"]["passive"].append({"name": m["skill"]["name"], "level":m["skill"]["level"]})

                lenas = len( dict[tmp[0]["id"]]["skills"]["active"] )
                if lenas < 6:
                    for i in range( 6 - lenas):
                        dict[tmp[0]["id"]]["skills"]["active"].append({"name":"Unknown", "level": "Unknown"})

                lenr = len( dict[tmp[0]["id"]]["skills"]["rune"] )
                if lenr < 6:
                    for i in range( 6 - lenr ):
                        dict[tmp[0]["id"]]["skills"]["rune"].append({"name":"Unknown", "level": "Unknown"})

                lenps = len( dict[tmp[0]["id"]]["skills"]["passive"] )
                if lenps < 3:
                    for i in range( 3 - lenps ):
                        dict[tmp[0]["id"]]["skills"]["passive"].append({"name":"Unknown", "level": "Unknown"})

            else:
                dict[tmp[0]["id"]]["skills"] = {}
                dict[tmp[0]["id"]]["skills"]["active"] = []
                dict[tmp[0]["id"]]["skills"]["passive"] = []
                dict[tmp[0]["id"]]["skills"]["rune"] = []

                for i in range( 6 ):
                    dict[tmp[0]["id"]]["skills"]["active"].append({"name":"Unknown", "level": "Unknown"})
                for i in range( 3 ):
                    dict[tmp[0]["id"]]["skills"]["passive"].append({"name":"Unknown", "level": "Unknown"})
                for i in range( 6 ):
                    dict[tmp[0]["id"]]["skills"]["rune"].append({"name":"Unknown", "level": "Unknown"})

            if "stats" in tmp[0]:
                #dict[tmp[0]["id"]]["stats"] = tmp[0]["stats"]
                dict[tmp[0]["id"]]["stats"] = {}
                if "dexterity" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["dexterity"] = "%.2f" % ((tmp[0]["stats"]["dexterity"]))
                else: dict[tmp[0]["id"]]["stats"]["dexterity"] = "0.00"

                if "damageIncrease" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["damageIncrease"] = "%.2f" % ((tmp[0]["stats"]["damageIncrease"]))
                else: dict[tmp[0]["id"]]["stats"]["damageIncrease"] = "0.00"

                if "lifeSteal" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["lifeSteal"] = "%.2f" % ((tmp[0]["stats"]["lifeSteal"]))
                else: dict[tmp[0]["id"]]["stats"]["lifeSteal"] = "0.00"

                if "intelligence" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["intelligence"] = "%.2f" % ((tmp[0]["stats"]["intelligence"]))
                else: dict[tmp[0]["id"]]["stats"]["intelligence"] = "0.00"

                if "blockAmountMin" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["blockAmountMin"] = "%.2f" % ((tmp[0]["stats"]["blockAmountMin"]))
                else: dict[tmp[0]["id"]]["stats"]["blockAmountMin"] = "0.00"

                if "arcaneResist" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["arcaneResist"] = "%.2f" % ((tmp[0]["stats"]["arcaneResist"]))
                else: dict[tmp[0]["id"]]["stats"]["arcaneResist"] = "0.00"

                if "fireResist" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["fireResist"] = "%.2f" % ((tmp[0]["stats"]["fireResist"]))
                else: dict[tmp[0]["id"]]["stats"]["fireResist"] = "0.00"

                if "secondaryResource" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["secondaryResource"] = "%.2f" % ((tmp[0]["stats"]["secondaryResource"]))
                else: dict[tmp[0]["id"]]["stats"]["secondaryResource"] = "0.00"

                if "strength" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["strength"] = "%.2f" % ((tmp[0]["stats"]["strength"]))
                else: dict[tmp[0]["id"]]["stats"]["strength"] = "0.00"

                if "blockAmountMax" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["blockAmountMax"] = "%.2f" % ((tmp[0]["stats"]["blockAmountMax"]))
                else: dict[tmp[0]["id"]]["stats"]["blockAmountMax"] = "0.00"

                if "armor" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["armor"] = "%.2f" % ((tmp[0]["stats"]["armor"]))
                else: dict[tmp[0]["id"]]["stats"]["armor"] = "0.00"

                if "damage" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["damage"] = "%.2f" % ((tmp[0]["stats"]["damage"]))
                else: dict[tmp[0]["id"]]["stats"]["damage"] = "0.00"

                if "blockChance" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["blockChance"] = "%.2f" % ((tmp[0]["stats"]["blockChance"]))
                else: dict[tmp[0]["id"]]["stats"]["blockChance"] = "0.00"

                if "life" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["life"] = "%.2f" % ((tmp[0]["stats"]["life"]))
                else: dict[tmp[0]["id"]]["stats"]["life"] = "0.00"

                if "critChance" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["critChance"] = "%.2f" % ((tmp[0]["stats"]["critChance"]))
                else: dict[tmp[0]["id"]]["stats"]["critChance"] = "0.00"

                if "damageReduction" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["damageReduction"] = "%.2f" % ((tmp[0]["stats"]["damageReduction"]))
                else: dict[tmp[0]["id"]]["stats"]["damageReduction"] = "0.00"

                if "vitality" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["vitality"] = "%.2f" % ((tmp[0]["stats"]["vitality"]))
                else: dict[tmp[0]["id"]]["stats"]["vitality"] = "0.00"

                if "goldFind" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["goldFind"] = "%.2f" % ((tmp[0]["stats"]["goldFind"]))
                else: dict[tmp[0]["id"]]["stats"]["goldFind"] = "0.00"

                if "lightningResist" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["lightningResist"] = "%.2f" % ((tmp[0]["stats"]["lightningResist"]))
                else: dict[tmp[0]["id"]]["stats"]["lightningResist"] = "0.00"

                if "magicFind" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["magicFind"] = "%.2f" % ((tmp[0]["stats"]["magicFind"]))
                else: dict[tmp[0]["id"]]["stats"]["magicFind"] = "0.00"

                if "poisonResist" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["poisonResist"] = "%.2f" % ((tmp[0]["stats"]["poisonResist"]))
                else: dict[tmp[0]["id"]]["stats"]["poisonResist"] = "0.00"

                if "coldResist" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["coldResist"] = "%.2f" % ((tmp[0]["stats"]["coldResist"]))
                else: dict[tmp[0]["id"]]["stats"]["coldResist"] = "0.00"

                if "lifePerKill" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["lifePerKill"] = "%.2f" % ((tmp[0]["stats"]["lifePerKill"]))
                else: dict[tmp[0]["id"]]["stats"]["lifePerKill"] = "0.00"

                if "critDamage" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["critDamage"] = "%.2f" % ((tmp[0]["stats"]["critDamage"]))
                else: dict[tmp[0]["id"]]["stats"]["critDamage"] = "0.00"

                if "primaryResource" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["primaryResource"] = "%.2f" % ((tmp[0]["stats"]["primaryResource"]))
                else: dict[tmp[0]["id"]]["stats"]["primaryResource"] = "0.00"

                if "physicalResist" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["physicalResist"] = "%.2f" % ((tmp[0]["stats"]["physicalResist"]))
                else: dict[tmp[0]["id"]]["stats"]["physicalResist"] = "0.00"

                if "attackSpeed" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["attackSpeed"] = "%.2f" % ((tmp[0]["stats"]["attackSpeed"]))
                else: dict[tmp[0]["id"]]["stats"]["attackSpeed"] = "0.00"

                if "lifeOnHit" in tmp[0]["stats"]:
                    dict[tmp[0]["id"]]["stats"]["lifeOnHit"] = "%.2f" % ((tmp[0]["stats"]["lifeOnHit"]))
                else: dict[tmp[0]["id"]]["stats"]["lifeOnHit"] = "0.00"


                
            else:
                print "!!! error!"
                #dict[tmp[0]["id"]]["stats"] = {}
                
            if "items" in tmp[0]:
                #dict[tmp[0]["id"]]["items"] = tmp[0]["items"]
                dict[tmp[0]["id"]]["items"] = {}
                if "head" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["head"] = tmp[0]["items"]["head"]["name"]
                else: dict[tmp[0]["id"]]["items"]["head"] = "Unknown"

                if "torso" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["torso"] = tmp[0]["items"]["torso"]["name"]
                else: dict[tmp[0]["id"]]["items"]["torso"] = "Unknown"

                if "feet" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["feet"] = tmp[0]["items"]["feet"]["name"]
                else: dict[tmp[0]["id"]]["items"]["feet"] = "Unknown"

                if "hands" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["hands"] = tmp[0]["items"]["hands"]["name"]
                else: dict[tmp[0]["id"]]["items"]["hands"] = "Unknown"

                if "legs" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["legs"] = tmp[0]["items"]["legs"]["name"]
                else: dict[tmp[0]["id"]]["items"]["legs"] = "Unknown"

                if "bracers" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["bracers"] = tmp[0]["items"]["bracers"]["name"]
                else: dict[tmp[0]["id"]]["items"]["bracers"] = "Unknown"

                if "mainHand" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["mainHand"] = tmp[0]["items"]["mainHand"]["name"]
                else: dict[tmp[0]["id"]]["items"]["mainHand"] = "Unknown"

                if "rightFinger" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["rightFinger"] = tmp[0]["items"]["rightFinger"]["name"]
                else: dict[tmp[0]["id"]]["items"]["rightFinger"] = "Unknown"

                if "waist" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["waist"] = tmp[0]["items"]["waist"]["name"]
                else: dict[tmp[0]["id"]]["items"]["waist"] = "Unknown"

                if "leftFinger" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["leftFinger"] = tmp[0]["items"]["leftFinger"]["name"]
                else: dict[tmp[0]["id"]]["items"]["leftFinger"] = "Unknown"

                if "neck" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["neck"] = tmp[0]["items"]["neck"]["name"]
                else: dict[tmp[0]["id"]]["items"]["neck"] = "Unknown"

                if "wrist" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["wrist"] = tmp[0]["items"]["wrist"]["name"]
                else: dict[tmp[0]["id"]]["items"]["wrist"] = "Unknown"

                if "jewelry" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["jewelry"] = tmp[0]["items"]["jewelry"]["name"]
                else: dict[tmp[0]["id"]]["items"]["jewelry"] = "Unknown"

                if "shoulders" in tmp[0]["items"]:
                    dict[tmp[0]["id"]]["items"]["shoulders"] = tmp[0]["items"]["shoulders"]["name"]
                else: dict[tmp[0]["id"]]["items"]["shoulders"] = "Unknown"
                
                
            else:
                print "!!! error!############"

            
            
            #tmp[0]["heroes"]

json.dump(dict, ofile)
