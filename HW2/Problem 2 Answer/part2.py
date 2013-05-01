import scipy.sparse
from collections import defaultdict
import json
import time
import pickle
import math
from scipy.io import *
#Also need to assign zero page rank for those neither mention anyone nor be mentioned


def Sort( finalVector, resultSize, title ):
    sortList = []
    i = 0
    for num in finalVector:
        sortList.append( ( num, i ) )
        i += 1
    sortList.sort( key = lambda x : x[ 0 ], reverse = True )
    j = 0
    while j < resultSize:
        userid = title[ sortList[ j ][ 1 ] ]
        print str(j+1) + ". ",
        print userid
        j += 1


def teleCal( teleVector, zeroRow, nZeroRow ):
    result1 = 0
    result2 = 0
    result = 0
    for i in nZeroRow:
        result1 += teleVector[ i ]
    result1 = result1 * teleporting * ( 1.0 / matrixSize )
    for i in zeroRow:
        result2 += teleVector[ i ]
    result2 = result2 * ( 1.0 / matrixSize )
    result = result1 + result2
    return [ result ] * matrixSize


def spaCal( finalVector, nZeroRowList, nZeroColList, mtx ):
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


# program basic parameters
teleporting = 0.1
resultSize = 50
iterNum = 100
threshold = 0.000001   #convergence threshold

#startTime = time.time()############

mtx = mmio.mmread( "sparse_matrix.mtx" )
mtx = mtx.tolil()

#print "Time1:" + str( time.time() - startTime )############

with open( 'title.pickle', 'rb' ) as f:
    title = pickle.load( f )
matrixSize = len( title )
print matrixSize
#print "Time2:" + str( time.time() - startTime )############

nZeroRowList = mtx.nonzero()[0]
nZeroColList = mtx.nonzero()[1]

nZeroRow = set( nZeroRowList )   #set 'nZeroRow' is used to store the not all zero rows in 'mtx'.
zeroRow = set( range( matrixSize ) ) - nZeroRow   #set 'zeroRow' is used to store the all zero rows in 'mtx'.

#initial vector
iniVector = [ 1.0 / matrixSize ] * matrixSize

iter_round = 1
while iter_round <= iterNum:
    
    #after this line, finalVector is a partial result of real finalVector. It is the result of iniVector and teleportation matrix
    finalVector = teleCal( iniVector, zeroRow, nZeroRow )

    #print "Time3:" + str( time.time() - startTime )############

    #calculate spaVector
    finalVector = spaCal( finalVector, nZeroRowList, nZeroColList, mtx )
    
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
Sort( finalVector, resultSize, title )

with open( "finalVector.pickle", "wb" ) as f:
    pickle.dump( finalVector, f );
