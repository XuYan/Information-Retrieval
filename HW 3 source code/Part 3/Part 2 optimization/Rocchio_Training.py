"""
The program is the training stage of Naive Bayes algorithm
"""

from collections import defaultdict
import json
import math
import re
import sys

def main():
    #category_dict structure:{"politics":["...",...], "business":["...",...],"entertainment":["...",...]}
    f = open( "docs.json", "r" )
    category_dict = json.loads( f.readline().strip('\n') )
    f.close()

    #determine the dimensions in the vector space
    #dimension structure:{ "w1":..., "w2":..., "w3":... }
    dimension = Vector_Space_dimension(category_dict)
    TF_IDF( category_dict, dimension )


def Vector_Space_dimension(category_dict):
    dimension = defaultdict(int)
    for category in category_dict:
        for doc in category_dict[category]:
            for term in doc.lower().split():
                if term in stop_word_list:
                    continue
                dimension[term] = 1
    print "dimension:" + str(len(dimension))
    return dimension

def TF_IDF(category_dict, dimension):
    doc_seq = 0
    df = defaultdict( int )
    doc_info = defaultdict(list)
    total_docs = 0

    for cat in category_dict:
        List = category_dict[cat]
        total_docs += len(List)
        for doc in List:
            tf = defaultdict( int )
            for word in doc.lower().split():
                if word in stop_word_list:
                    continue
                tf[word] += 1
            for word in tf:
                df[word] += 1
            for word in dimension:
                if word not in tf:
                    tf[word] = 0
            doc_info[cat].append(tf)     
    f = open("df.json","w")
    f.write( json.dumps(df) )
    f.close()


    for cat in doc_info:
        List = doc_info[cat]
        i = 0
        while i < len(List):
            Dict = List[i]
            for word in Dict:
                if Dict[word] != 0:
                    val = (1+math.log(Dict[word],2))*math.log(1.0*total_docs/df[word],2)
                else:
                    val = 0
                Dict[word] = val
            i += 1


    centroid = defaultdict(lambda:defaultdict(float))
    #determine centroids:
    for cat in doc_info:
        List = doc_info[cat]
        for word in List[0]:
            Sum = 0
            i = 0
            while i < len(List):
                Sum += List[i][word]
                i+=1
            centroid[cat][word] = 1.0*Sum / len(List)

    f = open("centroid.json","w")
    f.write( json.dumps(centroid) )
    f.close()


if __name__ == "__main__":
    stop_word_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','each','few','for','from','further','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself',"let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours' ]
    main()
