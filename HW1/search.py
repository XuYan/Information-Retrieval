import sys
import pickle

def main():
    para = 1
    elem = []
    temp = ''
    query = []
    wildcardList = []
    suitableList = []
    doublewildList = []
    count = 0

    if len( sys.argv ) == 1:
        print 'Usage: ./search.py "phrase" { keyword, "phrase" ... }'
        sys.exit(1)
    while para < len( sys.argv ):
        elem.append( sys.argv[ para ].lower() )
        para += 1
    #"token" is the same as token in command line
    for token in elem:
        if token.find( '*' ) != -1:
            if len( token ) < 3:
                print "wild card query item provides too little info"
                sys.exit( 2 )
            else:
                wildcardList.append( wildcardParse( token ) )
        elif token[ 0 ] == '"':
            temp += ( token + " " )
        elif token[ -1 ] == '"':
            temp += token
            query.append( temp[ 1:-1 ] )
            temp = ''
        else:
            query.append( token )
            
    #phrase+normal search result
    with open( 'index.pickle', 'rb' ) as f:
        Result = pickle.load( f )
        if len( query ) != 0:
            normalResult = search( query )#normalResult is the result of phrase/common query
            suitableList = normalResult[:]
            #when a possible word of wildcard search item is in the doc of normalResult, keep it;
            #if all the words of wildcard search item are not in the doc of normalResult, delete the doc from suitableList
            #This is an optimization. Separete the comparison of wildcard query and common/phrase query
            if len( normalResult ) != 0:
                if len( wildcardList ) != 0:
                    for doc in normalResult:
                        count = 0
                        while count < len( wildcardList ):
                            for word in wildcardList[ count ]:
                                if Result[ word ].has_key( doc ):
                                    break
                            if ( word == wildcardList[ count ][ -1 ] ) and ( Result[ word ].has_key( doc ) == False ):
                                suitableList.remove( doc )
                                break;
                            count += 1
                    print suitableList
                else:
                    print normalResult
            else:
                print "No match is found"
        elif len( wildcardList ) != 0:
            j = 0
            while j < len( wildcardList ):
                for item in wildcardList[ j ]:
                    for i in list( Result[ item ] ):
                        if i not in suitableList:
                            suitableList.append( i )
                j += 1
                doublewildList.append( suitableList )
                suitableList = []
            if len( doublewildList ) == 1:
                if len( doublewildList[ 0 ] ) == 0:#this case is true when we search red*
                    print "No match is found"
                    sys.exit( 7 )
                print doublewildList[ 0 ]
            if len( doublewildList ) >= 2:
                finalList = [ val for val in doublewildList[ 0 ] if val in doublewildList[ 1 ] ]
                countNum = 2
                while countNum < len( doublewildList ):
                    finalList = [ val for val in finalList if val in doublewildList[ countNum ] ]
                    countNum += 1
                print finalList  
        else:
            print "No match is found"
            
        


def wildcardParse( token ):
    #token: j*h, balti*, *rick
    #QList = [ $ab, ... ]
    QList = []
    with open( '3gram.pickle', 'rb' ) as g:
        kgramResult = pickle.load(g)
    #Add '$' directly to the head of 'token' for convenience
    newToken = '$' + token
    if newToken[ -1 ] == '*':
        newToken = newToken[ 0 : -1 ]
        for i in range( 0, len( newToken ) - 2 ):
            str = newToken[ i : i + 3 ]
            QList.append( str )
    else:
        delimeter = newToken.find( '*' )
        newToken = newToken[ (delimeter + 1) : ] + newToken[ 0 : delimeter ]
        for i in range( 0, len( newToken ) - 2 ):
            str = newToken[ i : i + 3 ]
            QList.append( str )
    #token as a parameter is for the comparison in function postFilter()
    return wildcardSearch( kgramResult, QList, token )
    

def wildcardSearch( kgramResult, QList, token ):
    #In QList: case 1: There is only one 3-gram index eg. h$j; case 2: There are more than one 3-gram index
    #tempList stores vocabulary [ 'baltimore', '',... ]
    for kgram in QList:
        if not kgramResult.has_key( kgram ):
            print "No match is found"
            sys.exit( 6 )
            
    if len( QList ) == 1:
        tempList = kgramResult[ QList[ 0 ] ]
    else:
        tempList = [ val for val in kgramResult[ QList[ 0 ] ]if val in kgramResult[ QList[ 1 ] ] ]
        num = 2
        while num < len( QList ):
            tempList = [ val for val in tempList if val in kgramResult[ QList[ num ] ] ]
            num += 1
        tempList = postFilter( tempList, token )#assign the processed word list to tempList again
    return tempList


def postFilter( tempList, token ):
    finalList = []
    if token[ 0 ] == '*':
        #case 1:*rick
        case = 1
        match = token[ 1 : ]
    elif token[ -1 ] == '*':
        #case 2:balti*
        case = 2
        match = token[ 0 : -1 ]
    else:
        #case 3:j*h
        case = 3
        fmatch = token[ 0 : token.find( '*' ) ]
        rmatch = token[ (token.find( '*' ) + 1) : ]

    if case == 1:
        for candidate in tempList:
            if candidate.find( match, -len(match) ) != -1:
                finalList.append( candidate )
    elif case == 2:
        for candidate in tempList:
            if candidate.find( match ) == 0:
                finalList.append( candidate )
    else:
        for candidate in tempList:
            if ( candidate.find( fmatch ) == 0 ) and ( candidate.find( rmatch, -len(rmatch) ) != -1 ):
                finalList.append( candidate )
    return finalList
        
def search( query ):
    dict = {}
    temp = []
    with open( 'index.pickle', 'rb' ) as f:
        Result = pickle.load( f )
        
        if len( query ) == 1:
            mylist = query[ 0 ].split()
            if len( mylist ) == 1:
                if( not Result.has_key( mylist[ 0 ] ) ):#this situation occurs when user try to search a non-existing word
                    print "No match is found"
                    sys.exit(4)
                dict = Result[ mylist[ 0 ] ]
                return list( dict )
                #temp.append( list( dict ) )
            else:
                return phraseParse( Result, mylist )
                #temp.append( phraseParse( Result, mylist ) )
        else:
            for token in query:
                term = token.split()
                if len( term ) == 1:
                    if( not Result.has_key( term[ 0 ] ) ):
                        print "No match is found"
                        sys.exit( 5 )
                    dict = Result[ term[ 0 ] ]
                    temp.append( list( dict ) )
                else:
                    temp.append( phraseParse( Result, term ) )
    #merge
    if len( temp ) >= 2:
        resultDoc = [ val for val in temp[ 0 ] if val in temp[ 1 ] ]
        num = 2
        while num < len( temp ):
            resultDoc = [ val for val in resultDoc if val in temp[ num ] ]
            num += 1
        #final result for phrase/normal search when search item >= 2
        return resultDoc
    #else:
        #return temp

    
    
def phraseParse( Result, mylist ):
    returnList = []
    if Result.has_key( mylist[ 0 ] ) and Result.has_key( mylist[ 1 ] ):
        commonDoc = [ val for val in list( Result[ mylist[ 0 ] ] ) if val in list( Result[ mylist[ 1 ] ] ) ]
    else:
        return returnList
    i = 2
    j = 1
    #find out the document in which all words apprear
    while i < len( mylist ):
        if Result.has_key( mylist[ i ] ):
            commonDoc = [ val for val in commonDoc if val in list( Result[ mylist[ i ] ] ) ]
            i += 1
        else:
            return returnList
    #check whether the words in phrase are really next to each other
    for doc in commonDoc:
        for pos in Result[ mylist[ 0 ] ][ doc ]:
            flag = True
            j = 1
            while j < len( mylist ):
                if (pos + j) in Result[ mylist[ j ] ][ doc ]:
                    j += 1
                else:
                    flag = False
                    break
            if flag == True:
                returnList.append( doc )
                break

    return returnList     
    
if __name__ == '__main__':
    main()
