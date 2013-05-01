import string
import pickle
import re

def preprocess():
    
    DocList = [ "19.txt", "23.txt", "35.txt", "36.txt", "46.txt",
                "61.txt", "70.txt", "71.txt", "74.txt", "76.txt",
                "86.txt", "91.txt", "93.txt", "95.txt", "98.txt",
                "102.txt", "107.txt", "110.txt", "119.txt", "130.txt",
                "132.txt", "142.txt", "144.txt", "153.txt", "155.txt",
                "159.txt", "203.txt", "217.txt", "219.txt", "220.txt",
                "236.txt", "245.txt", "269.txt", "271.txt", "297.txt",
                "364.txt", "376.txt", "384.txt", "388.txt", "399.txt",
                "416.txt", "421.txt", "430.txt", "451.txt", "456.txt",
                "460.txt", "469.txt", "471.txt", "474.txt", "479.txt",
                "493.txt", "494.txt", "495.txt", "496.txt", "500.txt",
                "503.txt", "507.txt", "525.txt", "526.txt", "527.txt",
                "530.txt", "535.txt", "536.txt", "543.txt", "597.txt",
                "608.txt", "619.txt", "638.txt", "655.txt", "687.txt",
                "693.txt", "711.txt", "712.txt", "752.txt", "815.txt",
                "816.txt", "820.txt", "832.txt", "847.txt", "898.txt",
                "910.txt", "980.txt", "996.txt" ]
    
    #strip = string.punctuation + "\"'"
    Result = {}
    kgramResult = {}
    
    with open( 'index.pickle', 'wb' ) as f:
        with open( '3gram.pickle', 'wb' ) as g:
            for i in DocList:
                pos = 1
                docID = int( i[ : -4 ] )
                fp = open( i, 'r' )
                myString = ""
            
                for line in fp.readlines():
                    myString += line

                for word in re.split( r"[-\s,.!?:;'\"]+", myString ):
                    word = word.lower()
                    
                #construct 3-gram indexes
                    if len( word ) > 1:
                        #pword is indexes used in 3-gram indexes
                        pword = word + '$'
                        for j in range( 0, len( pword ) ):
                            fir = j % len( pword )
                            sec = ( j + 1 ) % len( pword )
                            thi = ( j + 2 ) % len( pword )
                            str = pword[ fir ] + pword[ sec ] + pword[ thi ]
                            if kgramResult.has_key( str ):
                                if pword[ 0 : -1 ] not in kgramResult[ str ]:
                                    kgramResult[ str ].append( pword[ 0 : -1 ] )
                            else:
                                kgramResult[ str ] = []
                                kgramResult[ str ].append( pword[ 0 : -1 ] )

                    #construct positional indexes
                    if Result.has_key( word ):
                        if Result[ word ].has_key( docID ):
                            #record position
                            Result[ word ][ docID ].append( pos )
                        else:
                            Result[ word ][ docID ] = []
                            #record pos
                            Result[ word ][ docID ].append( pos )
                    else:
                        Result[ word ] = {}
                        Result[ word ][ docID ] = []
                        #record position
                        Result[ word ][ docID ].append( pos )
                    pos += 1
            pickle.dump( kgramResult, g )
        pickle.dump( Result, f )

preprocess()
