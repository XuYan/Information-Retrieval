from collections import defaultdict
from Queue import PriorityQueue
import re
import string
import math
import json
import pickle

showSize = 50   #the max number of relevant result shown to searcher

def preprocessing():

    #read finalVector of user pageranks from pickle file 'pagerank.pickle'
    with open( "finalVector.pickle", "rb" ) as f:
        finalVector = pickle.load( f )   #finalVector stores pagerank of all users
    with open( "title.pickle", "rb" ) as f:
        title = pickle.load( f )   #title stores userids of all users

    #parsing json file
    textList = []
    authorList = []
    f = open( "mars_tweets_medium.json", "r" )
    for line in f.readlines():
        dict = json.loads( line )
        textList.append( dict[ "text" ] )
        authorList.append( dict[ "user" ][ "id" ] )
    

    
    textID = 0
    tf_dict = defaultdict( lambda : defaultdict( int ) )   #I feel this structure for tf_dict {"textNum":{"term":tf}, ... } seems to be more appropriate
    idf_dict = defaultdict( int )
    finalScore = PriorityQueue()


    #Generate tf-idf dicts
    while textID < len( textList ):
    
        for term in re.split( r"[-#\s,.!?:;'\"]+", textList[ textID ] ):
            term = term.lower()
            tf_dict[ textID ][ term ] += 1
        for key in tf_dict[ textID ]:
            idf_dict[ key ] += 1
        textID += 1  

    #Receive user input
    while 1:
        string = raw_input( "Please input your query(-1 to quit)\n" )
        queryList = string.split()
        if( len(queryList) == 1 ) and ( queryList[ 0 ] == '-1' ):
            return
        else:
            #calculate query vector
            query_tf = defaultdict( int )
            QFlag = True
            for queryTerm in queryList:
                #if any query token does not occur in tweet corpus, return no result
                if idf_dict[ queryTerm ] == 0:
                    print "no match :-("
                    QFlag = False
                    break
                query_tf[ queryTerm ] += 1
            if QFlag:
                QVector = QueryVector( query_tf, idf_dict, len( textList ) )   #the structure of QVector will be {'bob':1.3, 'dog':2.0...}
                QVector = normalization( QVector )   #QVector has been normalized after this line

                #calculate text vector
                textNum = 0
                while( textNum < len( textList ) ): 
                    calculateFlag = False
                    for queryTerm in queryList:
                        if tf_dict[ textNum ].has_key( queryTerm ):
                            calculateFlag = True
                            break
                    if calculateFlag:
                        TVector = TextVector( tf_dict[ textNum ], idf_dict, len( textList ) )
                        TVector = normalization( TVector )
                        #obtain the pagerank of the author of this twitter:
                        authorID = authorList[ textNum ]
                        if authorID in title:
                            pos = title.index( authorID )
                            PR = finalVector[ pos ]
                        else:
                            PR = 0
                        #calculate final score of different texts:
                        finalScore.put( ( 1/ScoreCal( QVector, TVector, PR ), textNum ) )   #For PriorityQueue, the lower the first number is, the higher priority it has
                    textNum += 1
                printResult( finalScore, textList )
                
def TextVector( text_tf, idf_dict, textListSize ):
    TVector = defaultdict( float )
    for term in text_tf:
        termWeight = TermWeight( text_tf[ term ], idf_dict[ term ], textListSize )
        TVector[ term ] = termWeight
    return TVector

            
def QueryVector( query_tf, idf_dict, textListSize ):
    Qvector = defaultdict( float )
    for term in query_tf:
        termWeight = TermWeight( query_tf[ term ], idf_dict[ term ], textListSize )
        Qvector[ term ] = termWeight
    return Qvector


def TermWeight( tf, idf, textListSize ):
    return (1 + math.log( tf, 2 ) ) * math.log( ( float(textListSize)/idf ), 2 )


def normalization( Vector ):
    length = 0   #accumulate length
    for Term in Vector:
        length += math.pow( Vector[ Term ], 2 )
    length =  math.sqrt( length )
    for Term in Vector:
        Vector[ Term ] /= length
    return Vector


def ScoreCal( QVector, TVector, PR ):
    score = 0.0
    for term in QVector:
        if TVector.has_key( term ):
            score += QVector[ term ] * TVector[ term ]
    score += PR   #pagerank + tf-idf is final result
    return score


def printResult( finalScore, textList ):
    i = 0
    while i < showSize:
        i += 1
        if finalScore.empty() == False:
            reTextNum = finalScore.get()[ 1 ]
            print `i` + ". " + textList[ reTextNum ]
            
preprocessing()
