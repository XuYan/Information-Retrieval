from collections import defaultdict
import string
import re
import math
import kmeans
import json
import sys

def TF_IDF():
    doc_seq = 0
    df = defaultdict( int )
    doc_info = defaultdict()
    
    for doc in Doc_List:
        doc_tf = defaultdict( int )
        for word in re.findall( r'[0-9a-z]+', (doc[ 'title' ] + " " + doc[ 'description' ]).lower() ):
            doc_tf[ word ] += 1
        for word in doc_tf:
            df[ word ] += 1
        #doc_info's structure:{ 0:{ w0:1, w1:3,...}, 1:{w1:1, w2:1,...}, ...}
        doc_info[ doc_seq ] = doc_tf
        doc_seq += 1

    
    #calculate doc vectors:
    doc_seq = 0
    doc_num = len( doc_info )   #doc_num is the total number of docs( approximate 150)
    doc_collection = []         #it will be returned from the function
    while doc_seq < doc_num:
        doc_vector = defaultdict( float )
        for word in df:
            if word in doc_info[ doc_seq ]:
                #doc_vector's structure: {w0:2,w1:0,w2:0,w3:3,...}
                doc_vector[ word ] = (1.0 + math.log(doc_info[ doc_seq ][ word ],2) ) * math.log( (1.0 * len(doc_info) / df[ word ]),2)
            else:
                doc_vector[ word ] = 0.0
        doc_seq += 1
        doc_collection.append( doc_vector )

    return doc_collection
     


if __name__ == "__main__":
    Doc_List = []                       #structure:[{'Description':...,'Title':...},{'Description':...,'Title':...},...]
    Title_List = []                     #structure:[ 'Title1', 'Title2',...]

    #Extract doc_list from "docs.txt"
    f = open( 'docs.json', 'r' )
    for doc in f.readlines():
        #Remove the '\n' at the end of doc
        doc = doc.strip('\n')
        doc_dict = json.loads( doc )
        Doc_List.append( doc_dict )
        #obtain Title_List
        Title_List.append( doc_dict[ 'title' ] )       
    f.close()
    
    #Calculate tf-idf of each word in each doc:
    #doc_collection's structure: [doc_vector1,doc_vector2,...]
    #doc_vector's structure:{word1:tf-idf val, word2:tf-idf val,...}
    doc_collection = TF_IDF()
    
    #this block will generate value_collection. Its structure is: [[1,2,0,1,2,...],[0,2,1,3,0...],...]
    value_collection = []
    for doc_vector in doc_collection:
        doc_value = []
        for word in doc_vector:
            doc_value.append( doc_vector[ word ] )
        value_collection.append( doc_value )

    #print value_collection
    #K Means is coming!
    k = raw_input( "Please input a value for k: " )
    k = int( k )
    
    KMeans = kmeans.k_means( k )
    
    KMeans.K_MEANS( value_collection, Title_List )
