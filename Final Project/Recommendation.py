from collections import defaultdict
import math
import json
import sys

def Career_Recommendation( career_property, user_input ):
    score_dict = defaultdict(float)
    
    for career in career_property:
        score = 0.0
        normalization_factor1 = 0.0
        normalization_factor2 = 0.0
        for property in career_property[ career ]:
            score += career_property[ career ][ property ] * user_input[ property ]
            normalization_factor1 += math.pow( career_property[ career ][ property ], 2 )
            normalization_factor2 += math.pow( user_input[ property ], 2 )
        score_dict[ career ] = 1.0 * score / ( math.sqrt(normalization_factor1) * math.sqrt(normalization_factor2) )

    """
    with open( "careerProbability.json" ) as f:
        career_probability = json.loads( f.readline() )
    """
    #print score_dict
    
    score_list = sorted( score_dict.values(), reverse = True )
    career_recommendation = []
    for score in score_list:
        for career in score_dict:
            if score_dict[career] == score:
                career_recommendation.append( career )
    return score_dict, career_recommendation


def Friend_Recommendation( user_timePlayed, score_dict ):
    pos_score_dict = normalization( score_preprocessing( score_dict ) )
    pos_user_timePlayed = defaultdict(float)
    Friend_score = defaultdict(float)
    
    for user in user_timePlayed:
        pos_user_timePlayed[user] = normalization( user_timePlayed[user] )

    for user in user_timePlayed:
        Friend_score[user] = getScore( pos_user_timePlayed[user], pos_score_dict )

    sorted_score_list = sorted( Friend_score.values(), reverse = True )
    friend_recommendation = []
    
    return sorted(Friend_score, key = Friend_score.get, reverse = True)[:10]


def getScore( mydict1, mydict2 ):
    score = 0.0
    for career in mydict1:
        score += mydict1[career] * mydict2[career]
    return score


def normalization( mydict ):
    new_dict = defaultdict()
    value = 0.0
    for career in mydict:
        value += math.pow( mydict[career], 2 )
    value = math.sqrt( value )
    for career in mydict:
        #mydict[career] = 1.0 * mydict[career] / value
        new_dict[career] = 1.0 * mydict[career] / value
    return new_dict

def score_preprocessing( score_dict ):
    '''
    max_neg = -1 * sys.maxint
    for career in score_dict:
        if score_dict[career] > max_neg:
            max_neg = score_dict[career]
    for career in score_dict:
        score_dict[career] = 1.0 * max_neg / score_dict[career]
    return score_dict
    '''
    max_float = 0.0
    min_float = 100.0
    for career in score_dict:
        if score_dict[ career ] > max_float:
            max_float = score_dict[ career ]
        if score_dict[ career ] < min_float:
            min_float = score_dict[ career ]

    gap = max_float - min_float
    for career in score_dict:
        score_dict[ career ] = 1.0 * ( score_dict[ career ] - min_float ) / gap
    #print score_dict

    return score_dict


def getInput( user_input ):
    career_property = {"barbarian":{"Melee":1.0,"Range":0.4,"Tank":1.0,"Support":0.4,"Damage":1.0,"Solo":1.0,"Team":1.0,"Physical":1.0,"Magical":0.2},
                       "demon-hunter":{"Melee":0.2,"Range":1.0,"Tank":0.2,"Support":0.6,"Damage":1.0,"Solo":0.8,"Team":1.0,"Physical":0.8,"Magical":0.8},
                       "wizard":{"Melee":0.2,"Range":1.0,"Tank":0.4,"Support":0.6,"Damage":1.0,"Solo":0.8,"Team":1.0,"Physical":0.2,"Magical":1.0},
                       "monk":{"Melee":1.0,"Range":0.4,"Tank":0.6,"Support":1.0,"Damage":1.0,"Solo":1.0,"Team":1.0,"Physical":1.0,"Magical":0.2},
                       "witch-doctor":{"Melee":0.4,"Range":0.8,"Tank":0.6,"Support":0.8,"Damage":0.8,"Solo":1.0,"Team":1.0,"Physical":1.0,"Magical":0.8}}

    #user_input = {"Melee":5,"Range":2,"Tank":3,"Support":5,"Damage":5,"Solo":5,"Team":5,"Physical":5,"Magical":1}#!!!!!!

########
    for property in user_input:
        user_input[ property ] /= 5.0;
########
        
    score_dict, career_recommendation = Career_Recommendation( career_property, user_input )
    print career_recommendation
    with open( "timePlayed.json" ) as g:
        user_timePlayed = json.loads( g.readline() )
    friend_recommendation = Friend_Recommendation( user_timePlayed, score_dict )
    print friend_recommendation

    return career_recommendation, friend_recommendation
    '''
    i = 0
    for user in friend_recommendation:
        print str( i ) + str( user_timePlayed[ user ] )
    '''
