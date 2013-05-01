'''
For example, there are three clusters
centroid_collection structure:[[1,2,5,3,...],[3,2,4,6,...],[4,5,6,3,...]]
cluster structure:{1:[[1,2,3,...],[5,4,3,...],[4,7,5,...]...],2:[[],[],[]...],3:[[],[],[]...]}
'''
import math
def RSS_Calculation( centroid_collection, cluster ):
    i = 0
    RSS = 0.0
    while i < len(centroid_collection):
        for point in cluster[i]:
            RSS += dis( centroid_collection[i],point )
        i += 1
    return RSS

def dis( centroid, point ):
    i = 0
    val = 0.0
    while i < len( centroid ):
        val += math.pow( (point[i] - centroid[i]), 2 )
        i += 1
    return math.sqrt(val)

