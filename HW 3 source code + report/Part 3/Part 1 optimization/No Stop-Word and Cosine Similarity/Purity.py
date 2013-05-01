import json
import math
import sys
from collections import defaultdict

def purity( title, title_cluster, doc_num ):
    '''
        RI_List is used to store cluster_result in every cluster
    '''
    RI_List = []
    '''
        For each cluster, find out the intersections with each query class
        return the max one
    '''
    result = 1.0
    for cluster_num in title_cluster:
        cluster_result = defaultdict( int )
        for doc_title in title_cluster[ cluster_num ]:
            if doc_title in title[ 'texas aggies' ]:
                cluster_result[ 'texas aggies' ] += 1
            elif doc_title in title[ 'texas longhorns' ]:
                cluster_result[ 'texas longhorns' ] += 1
            elif doc_title in title[ 'duke blue devils' ]:
                cluster_result[ 'duke blue devils' ] += 1
            elif doc_title in title[ 'dallas cowboys' ]:
                cluster_result[ 'dallas cowboys' ] += 1
            elif doc_title in title[ 'dallas mavericks' ]:
                cluster_result[ 'dallas mavericks' ] += 1
        result += findMax( cluster_result )
        RI_List.append( cluster_result )
    purity = 1.0 * result / doc_num
    print "Purity is " + str(purity)

    RI = RI_Calculation( RI_List )
    print "Rand Index is " + str(RI)


def RI_Calculation(RI_List):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    TPFP = 0
    total_point = 0
    '''
        RI_List is a list of dictionaries
        cluster is a dictionary with structure: { 'texas aggies' : 2, 'texas longhorns' : 5 }
        Pay attention that the dictionary may not contain all the five queries as keys
    '''
    for cluster in RI_List:
        cluster_total_point = 0
        if (len(cluster) == 1) and (cluster.values()[0] == 1):
            cluster_total_point += 1
        else:
            for query_class in cluster:
                cluster_total_point += cluster[ query_class ]
                if cluster[ query_class ] > 1:
                    TP += C( cluster[ query_class ],2 )
            TPFP += C( cluster_total_point,2 )
        total_point += cluster_total_point

    TPTNFPFN = C(total_point,2)
    TNFN = TPTNFPFN - TPFP

    '''
        Calculate FN
    '''
    i = 0
    while i < len(RI_List):
        j = i + 1
        while j < len(RI_List):
            for key in RI_List[ i ]:
                if key in RI_List[ j ]:
                    FN += RI_List[ i ][ key ] * RI_List[ j ][ key ]
            j += 1
        i += 1

    TN = TNFN - FN

    return 1.0 * ( TP + TN ) / TPTNFPFN
        
'''
    This is for combination calculation
'''
def C( lower, upper ):
    if lower < upper:
        print "Error Detected!"
        sys.exit()
    numerator = math.factorial(lower) / math.factorial( lower - upper )
    denomitor = math.factorial( upper )

    return 1.0 * numerator / denomitor
    


def findMax( cluster_result ):
    Max = 0
    for cluster in cluster_result:
        if cluster_result[ cluster ] > Max:
            Max = cluster_result[ cluster ]
    return Max


def main():

    '''
        title is a dictionary with structure {'texas aggies':[...], 'texas longhorns':[...], ...}
        title_cluster is a dictionary with structure { '1':[...],'2':[...],...}
    '''

    
    f = open( "title.json", "r" )
    title = json.loads( f.readline() )
    f.close()

    f = open( "title_cluster.json", "r" )
    title_cluster = json.loads( f.readline() )
    f.close()

    purity( title, title_cluster, 150 )
    

if __name__ == "__main__":
    main()
