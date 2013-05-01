from collections import defaultdict
import random
import math
import json
import RSS
import sys

class k_means():

    def __init__( self, k ):
        self.k = k

    #node_list's structure:[[1,2,0,1,2,...],[0,2,1,3,0...],...]
    def K_MEANS( self, node_list, Title_List ):
        #dimension of the vector space. (# of unique words in the docs)
        dimension = len( node_list[ 0 ] )
        seed = []
        temp = 0

        #randomly picking k seeds(centroids)
        i = 1
        while i <= self.k:
            point_num = random.randint( 0, len(node_list) - 1 )
            #show initial centroids:
            if node_list[ point_num ] in seed:
                i -= 1
            else:
                seed.append( node_list[ point_num ] )
                '''print "Centroid " + str(i) + " is " + str(node_list[point_num])'''
            i += 1

        '''print "There are " + str( len( node_list ) ) + " documents in the space"'''

        Stable = False
        while not Stable:
            '''print "~~~~~~~~~~~~~~~~~~~~~~~~~"'''
            old_centroid = []
            for centroid in seed:
                old_centroid.append(centroid)
            '''print "New centroids are " + str(seed)'''
            
            cluster = defaultdict( list )
            i = 0

            #record the titles of docs included in a cluster 
            title_cluster = defaultdict( list )
            while i < len( node_list ):
                j = self.MinDistance( seed, node_list[ i ] )
                '''print "nearest centroid for node " + str(node_list[i]) + " is " + str(seed[j])'''
                title_cluster[ j ].append( Title_List[ i ] )
                cluster[ j ].append( node_list[ i ] )           #reassignment of vectors
                i += 1

            print "~~~~~~~~~"
            print "RSS is " + str( RSS.RSS_Calculation(seed,cluster) )
            
            i = 0
            while i < self.k:
                #sum_list record the sum of each dimension of each doc in a cluster
                #its structure is [1+2+3+...,1+2+0+...,]
                sum_list = []               
                point_list = cluster[ i ]   #point_list contains several points in cluster i
                j = 0
                while j < dimension:
                    for points in point_list:
                        temp += points[ j ]
                    sum_list.append( temp )
                    temp = 0
                    j += 1

                seed[ i ] = []
                for val in sum_list:
                    seed[ i ].append( 1.0 * val / len( point_list ) )   #recomputation of centroids

                i += 1
            '''print "old_centroid is " + str(old_centroid)'''
            if old_centroid == seed:
                print "Stable"
                Stable = True
                
        f = open( 'title_cluster.json', 'w' )
        f.write( json.dumps( title_cluster ) )
        f.close()
        
        print "The clusters are shown below( represented by title ):"
        for cluster_Num in title_cluster:
            print "Cluster " + str(cluster_Num) + ":"
            for title in title_cluster[ cluster_Num ]:
                print title
            print ""
    
    #Cluster using Cosine Similarity
    def MinDistance( self, seed, node ):
        Max = 0
        pos = 0
        for centroid_list in seed:
            similarity = self.Cosine_Similarity( centroid_list, node )
            if similarity > Max:
               Max = similarity
               pos = seed.index(centroid_list)
        return pos


    def Cosine_Similarity( self, centroid_list, node ):
        i = 0
        nominator = 0
        denominator_centroid_list = 0
        denominator_node = 0
        while i < len(centroid_list):
            nominator += centroid_list[ i ] * node[ i ]
            denominator_centroid_list += math.pow(centroid_list[ i ],2)
            denominator_node += math.pow(node[ i ],2)
            i += 1
        return 1.0 * nominator / (math.sqrt(denominator_centroid_list)*math.sqrt(denominator_node))
