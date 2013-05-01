from scipy.io import *
import scipy.sparse
import json
from collections import defaultdict
import pickle

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


mydict = parseJson( "mars_tweets_medium.json" )

title = [] #list 'title' is the row/column of sparse matrix 'mtx'. It stores userids
# this 'for' loop will generate list 'title', which will not include anyone that neither mentions anyone nor was mentioned by anyone else
for person in mydict:
    if person not in title:
        title.append(person)
    mention = mydict[ person ]
    for mperson in mention:
        if mperson not in title:
            title.append(mperson)

matrixSize = len(title)

mtx = scipy.sparse.lil_matrix( ( matrixSize, matrixSize ) )
for person in title:
    if mydict[ person ] == []:
        pass
    else:
        row = title.index( person )
        prob = len( mydict[ person ] )
        for mentionName in mydict[ person ]:
            column = title.index( mentionName )
            mtx[ row, column ] = 1.0 / prob


mmio.mmwrite( "sparse_matrix", mtx )
with open( 'title.pickle', 'wb' ) as f:
    pickle.dump( title, f )
