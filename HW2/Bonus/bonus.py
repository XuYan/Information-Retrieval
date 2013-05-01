import scipy.sparse
from collections import defaultdict
import json
import math
import random
#Also need to assign zero page rank for those neither mention anyone nor be mentioned


def Sort( finalVector, resultSize, title, person_topic ):
    resultDict = defaultdict( list )
    sortList = []
    i = 0
    for num in finalVector:
        sortList.append( ( num, i ) )
        i += 1
    sortList.sort( key = lambda x : x[ 0 ], reverse = True )
    j = 0
    while j < resultSize:
        userid = title[ sortList[ j ][ 1 ] ]
        resultDict[ person_topic[ userid ] ].append( userid )
        j += 1
        
    for i in resultDict:
        print "topic '" + i + "' top user: "
        j = 0
        while j < 3:
            print str( j+1 ) + ". " + str( resultDict[ i ][ j ] )
            j += 1

def teleCalPre( iniVector, topicPosDict, zeroRow, teleporting ):
    topicValueDict = defaultdict()
    for topic in topicPosDict:
        value = 0
        length = len( topicPosDict[ topic ] )
        for pos in topicPosDict[ topic ]:
            if pos in zeroRow:
                value += iniVector[ pos ] * ( 1.0 / length ) * teleporting
            else:
                value += iniVector[ pos ] * ( 1.0 / length )
        topicValueDict[ topic ] = value
    return topicValueDict


def teleCal( topicValueDict, topicPosDict, matrixSize ):
    vector = [ 0 ] * matrixSize
    for topic in topicPosDict:
        for pos in topicPosDict[ topic ]:
            vector[ pos ] = topicValueDict[ topic ]
    return vector



def spaCal( finalVector, nZeroRowList, nZeroColList, mtx, teleporting ):
    coordinateList = []
    i = 0
    while i < len( nZeroRowList ):
        item = ( nZeroRowList[ i ], nZeroColList[ i ] )
        coordinateList.append( item )
        i += 1
    coordinateList.sort( key = lambda x : x[ 1 ] )
    
    for co in coordinateList:
        row = co[ 0 ]
        col = co[ 1 ]
        finalVector[ col ] += mtx[ row, col ] * iniVector[ row ] * ( 1 - teleporting )
    return finalVector


def parseJson( filename ):
    mydict = defaultdict( list )
    f = open( filename, "r" )
    for line in f.readlines():
        dict = json.loads( line )
        for tempDict in dict[ 'entities' ][ 'user_mentions' ]:
            if dict[ 'user' ][ 'id' ] ==  tempDict[ 'id' ]:
                pass
            else:
                if tempDict[ 'id' ] not in mydict[ dict[ 'user' ][ 'id' ] ]:
                    mydict[ dict[ 'user' ][ 'id' ] ].append( tempDict[ 'id' ] )   
    return mydict

# program basic parameters
teleporting = 0.1
resultSize = 4500
iterNum = 80
threshold = 0.000001   #convergence threshold

#startTime = time.time()############


mydict = parseJson( "mars_tweets_medium.json" )

title = [] #list 'title' is the row/column of sparse matrix 'mtx'. It stores userids

topicList = [ "Arts", "Business", "Computers", "Games",
              "Health", "Home", "Kids and Teens", "News",
              "Recreation", "Reference", "Regional", "Science",
              "Shopping", "Society", "Sports", "World" ]
topicDict = defaultdict( list )
person_topic = defaultdict()
tupleList = []
topicPosDict = defaultdict( list )


# this 'for' loop will generate list 'title', which will not include anyone that neither mentions anyone nor was mentioned by anyone else
for person in mydict:
    if person not in title:
        title.append(person)
        #assign a label for each userid randomly
        topicNum = random.randint( 0, 15 )
        topicName = topicList[ topicNum ]
        topicDict[ topicName ].append( person )
        topicPosDict[ topicName ].append( title.index( person ) )
        person_topic[ person ] = topicName
    mention = mydict[ person ]
    for mperson in mention:
        if mperson not in title:
            title.append(mperson)
            topicNum = random.randint( 0, 15 )
            topicName = topicList[ topicNum ]
            topicDict[ topicName ].append( mperson )
            topicPosDict[ topicName ].append( title.index( mperson ) )
            person_topic[ mperson ] = topicName

matrixSize = len(title)

mtx = scipy.sparse.lil_matrix( ( matrixSize, matrixSize ) )
for person in title:
    if mydict[ person ] == []:
        pass
    else:
        row = title.index( person )
        topicFlag = person_topic[ person ]
        prob = 0
        tupleList = []
        for mentionName in mydict[ person ]:
            column = title.index( mentionName )
            compFlag = person_topic[ mentionName ]
            if topicFlag == compFlag:
                prob += 1
                tupleList.append( ( row, column ) )
        for i in tupleList:
            row = i[ 0 ]
            column = i[ 1 ]
            mtx[ row, column ] = 1.0 / prob
#print "Time2:" + str( time.time() - startTime )############


nZeroRowList = mtx.nonzero()[0]
nZeroColList = mtx.nonzero()[1]

nZeroRow = set( nZeroRowList )   #set 'nZeroRow' is used to store the not all zero rows in 'mtx'.
zeroRow = set( range( matrixSize ) ) - nZeroRow   #set 'zeroRow' is used to store the all zero rows in 'mtx'.

iniVector = [ 1.0 / matrixSize ] * matrixSize   #initial vector


iter_round = 1
while iter_round <= iterNum:

    topicValueDict = teleCalPre( iniVector, topicPosDict, zeroRow, teleporting )
  
    #after this line, finalVector is a partial result of real finalVector. It is the result of iniVector and teleportation matrix
    finalVector = teleCal( topicValueDict, topicPosDict, matrixSize )

    #print "Time3:" + str( time.time() - startTime )############

    #calculate spaVector
    finalVector = spaCal( finalVector, nZeroRowList, nZeroColList, mtx, teleporting )
    
    #print "Time4:" + str( time.time() - startTime )############

    iter_round += 1
    j = 0
    diff = 0.0
    while j < len( finalVector ):
        diff += math.fabs( finalVector[ j ] - iniVector[ j ] )
        if diff > threshold:
            break
        j += 1
    if j == len( finalVector ):
        print iter_round - 1
        print "Converge!"
        break
    iniVector = finalVector

Sort( finalVector, resultSize, title, person_topic )
