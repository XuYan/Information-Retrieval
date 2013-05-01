from collections import defaultdict
import random
import math
import RSS

def clustering(doc_vector,k,Category_Doc):
    final_value_list = []
    final_title_list = []

    #dict to list: split doc_vector into two lists
    title_list=[]
    value_list=[]

    for title in doc_vector:
        title_list.append(title)
        values=[]
        for term in doc_vector[title]:
            values.append(doc_vector[title][term])
        value_list.append(values)
    while True:
        flag = True
        while flag:
            #select centroids
            i = 0
            seed = []
            while i < 2:
                candidate = random.randint( 0, len(value_list) - 1 )
                if value_list[candidate] in seed:
                    pass
                else:
                    seed.append(value_list[candidate])
                    i += 1
            #mark clustering process completion
            Stable = False
            while not Stable:
                #record previous centroids
                old_centroid = []
                for centroid in seed:
                    old_centroid.append(centroid)
                #Reassignment of vectors
                #cluster records the vectors in a cluster
                #title_cluster records the titles of docs included in a cluster
                cluster = defaultdict( list )
                title_cluster = defaultdict( list )
                i = 0
                while i < len( title_list ):
                    j = MinDistance( seed, value_list[i] )
                    cluster[ j ].append( value_list[ i ] ) #reassignment of vectors
                    title_cluster[ j ].append( title_list[ i ] )
                    i += 1

                #Recomputation of centroids
                dimension = len(value_list[0])
                i = 0
                while i < 2:
                    #sum_list records the sum of each dimension of each doc in a cluster
                    #its structure is [1+2+3+...,1+2+0+...,]
                    #point_list contains several points in cluster i
                    sum_list = []
                    point_list = cluster[ i ]
                    j = 0
                    temp = 0
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

                if old_centroid == seed:
                    Stable = True
                    print "Stable"
            print "RSS is " + str( RSS.RSS_Calculation(seed,cluster) )
            sat = raw_input("Satisfied with this RSS?(Y/N)")
            if sat == 'Y':
                flag = False
            else:
                flag = True
        final_title_list.append(title_cluster[0])
        final_title_list.append(title_cluster[1])
        final_value_list.append(cluster[0])
        final_value_list.append(cluster[1])
        if len(final_title_list) != int(k):
            #find out the cluster with more elements
            i = max_len(final_title_list)
            title_list = final_title_list[i]
            value_list = final_value_list[i]
            final_title_list.remove(title_list)
            final_value_list.remove(value_list)
        else:
            break
    i = 0
    while i < len(final_title_list):
        print "~~~~~~~~~~~~~~~~~~"
        print final_title_list[i]
        i += 1
    print Purity(Category_Doc, final_title_list)

def Purity(Category_Doc, final_title_list):
    total = 0
    doc_num = 0
    for title_cluster in final_title_list:
        count = defaultdict(int)
        print len(title_cluster)
        doc_num += len(title_cluster)
        for title in title_cluster:
            if title in Category_Doc["texas aggies"]:
                count["texas aggies"] += 1
            elif title in Category_Doc["texas longhorns"]:
                count["texas longhorns"] += 1
            elif title in Category_Doc["duke blue devils"]:
                count["duke blue devils"] += 1
            elif title in Category_Doc["dallas cowboys"]:
                count["dallas cowboys"] += 1
            else:
                count["dallas mavericks"] += 1
        total += Max(count)
    print doc_num
    return 1.0 * total /doc_num

def Max(count):
    max_num = count["texas aggies"]
    for category in count:
        if count[category] > max_num:
            max_num = count[category]
    return max_num


def max_len(final_title_list):
    Maxnum = 0
    Maxlen = len( final_title_list[0] )
    i = 1
    while i < len(final_title_list):
        if len(final_title_list[i]) > Maxlen:
            Maxnum = i
        i+=1
    return Maxnum

#Cluster using Cosine Similarity
def MinDistance( seed, node ):
    Max = 0
    pos = 0
    for centroid_list in seed:
        similarity = Cosine_Similarity( centroid_list, node )
        if similarity > Max:
            Max = similarity
            pos = seed.index(centroid_list)
    return pos

def Cosine_Similarity( centroid_list, node ):
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