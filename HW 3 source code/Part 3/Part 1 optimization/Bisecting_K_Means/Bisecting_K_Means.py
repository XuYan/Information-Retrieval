from collections import defaultdict
import K_Means
import json
import math
import sys
import re

def main():
    '''
    Title_Doc_Dict structure:
    {
        "Aggies Can't Avoid the Sweep":"Aggies Can't Avoid the Sweep blah blah..."
        ...
    }
    '''
    Title_Doc_Dict = defaultdict()
    Category_Doc = defaultdict()

    f = open( "docs.json", "r" )
    for doc in f.readlines():
        doc = doc.strip("\n")
        temp = json.loads(doc)
        Title_Doc_Dict[temp["title"]] = temp["title"] + " " + temp["description"]
    f.close()

    g = open("title.json","r")
    Category_Doc = json.loads(g.readline().strip("\n"))
    g.close()

    doc_vector = TF_IDF(Title_Doc_Dict)

    cluster_num = raw_input("Please input how many clusters you want:")
    K_Means.clustering(doc_vector,cluster_num, Category_Doc)


def TF_IDF(Title_Doc_Dict):
    '''
        doc_vector structure:
        {
            "Aggies Can't Avoid the Sweep":{
                                                'aggies':2, 'up':0, 'avoid':1,...
                                           }
            "Aggies up two spots to seventh at SDSU Farms Invitational":{
                                                                            'aggies':2, 'up':2, 'avoid':0...
                                                                        }
            ...
        }
    '''
    stop_word_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','each','few','for','from','further','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself',"let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours' ]
    df = defaultdict(int)
    temp = defaultdict()

    for doc_title in Title_Doc_Dict:
        tf = defaultdict(int)
        for token in re.findall(r'[0-9a-z]+', Title_Doc_Dict[doc_title].lower()):
            if token not in stop_word_list:
                tf[token] += 1
        for term in tf:
            df[term] += 1
        temp[doc_title] = tf

    doc_vector = defaultdict(lambda:defaultdict(float))
    for doc_title in Title_Doc_Dict:
        for term in df:
            if temp[doc_title].has_key(term):
                doc_vector[doc_title][term] = (1.0 + math.log(temp[doc_title][term],2) ) * math.log( (1.0 * len(Title_Doc_Dict) / df[term]),2)
            else:
                doc_vector[doc_title][term] = 0.0

    return doc_vector

if __name__ == "__main__":
    main()