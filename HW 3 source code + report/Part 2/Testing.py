import requests
import json
import math
from collections import defaultdict
import sys

def main():
    #category_dict structure:
    #{'apple':{'politics':[...,...,...],
    #          'business':[...,...,...],
    #          'entertainment':[...,...,...]
    #         }
    # 'facebook':{'politics':[...,...,...],
    #             'business':[...,...,...],
    #             'entertainment':[...,...,...]
    #            }
    #   ...
    #}
    f = open( "TestDocs.json" , 'r' )
    category_dict = json.loads( f.readline().strip( '\n' ) )
    f.close()

    #trainging_info structure:
    #{"politics":{"word_probability":{"all":...,"four":...,...},"class_probability":...,"class_tokens":...},
    # "business":{"word_probability":{"all":...,"four":...,...},"class_probability":...,"class_tokens":...},
    # "entertainment":{"word_probability":{"all":...,"four":...,...},"class_probability":...,"class_tokens":...}
    #}
    g = open( "TrainingResult.json", 'r' )
    training_info = json.loads( g.readline().strip( '\n' ) )
    g.close()

    
    print len(training_info["politics"]["word_probability"])
    print len(training_info["business"]["word_probability"])
    print len(training_info["entertainment"]["word_probability"])

    Test( category_dict, training_info )

    
def Test( category_dict, training_info ):
    length = TrainingSetLen( training_info["politics"]["word_probability"], training_info["business"]["word_probability"], training_info["entertainment"]["word_probability"] )
    
    classification_dict = defaultdict( list )
    for my_query in category_dict:
        print "~~~~~~~~~~~~~~~~~~"
        print "Query:" + my_query
        for category in category_dict[ my_query ]:
            print "Search Category(Ground Truth):" + category
            category_list = category_dict[ my_query ][ category ]
            for doc in category_list:
                classified_as = Classification( doc, training_info, length )
                print "Classified as " + classified_as
                classification_dict[category].append( classified_as )
    print "Microaveraging F is " + str(Microaveraging(classification_dict))

#classification_dict structure:
#{"politics":[p,b,...],
# "business":[b,e,b..],
# "entertainment":[e,b,...]
#}
def Microaveraging(classification_dict):
    #total number of docs retrieved for this query. It should be 90 in this case
    total_doc = len(classification_dict['politics'])+len(classification_dict['business'])+len(classification_dict['entertainment'])
    
    tp_p = 0
    fp_p = 0
    tn_p = 0
    fn_p = 0
    
    for classified_as in classification_dict['politics']:
        if classified_as == 'politics':
            tp_p += 1
        else:
            fn_p += 1
    for classified_as in classification_dict['business']:
        if classified_as == 'politics':
            fp_p += 1
    for classified_as in classification_dict['entertainment']:
        if classified_as == 'politics':
            fp_p += 1
    tn_p = total_doc - (tp_p + fp_p + fn_p)

    print "For politics:"
    print "~~~~~~"
    print "tp:" + str(tp_p)
    print "fp:" + str(fp_p)
    print "fn: " + str(fn_p)
    print "tn: " + str(tn_p)
    print "~~~~~~"

    tp_b = 0
    fp_b = 0
    tn_b = 0
    fn_b = 0
    for classified_as in classification_dict['business']:
        if classified_as == 'business':
            tp_b += 1
        else:
            fn_b += 1
    for classified_as in classification_dict['politics']:
        if classified_as == 'business':
            fp_b += 1
    for classified_as in classification_dict['entertainment']:
        if classified_as == 'business':
            fp_b += 1
    tn_b = total_doc - (tp_b + fp_b + fn_b)

    print "For business:"
    print "~~~~~~"
    print "tp:" + str(tp_b)
    print "fp:" + str(fp_b)
    print "fn: " + str(fn_b)
    print "tn: " + str(tn_b)
    print "~~~~~~"

    tp_e = 0
    fp_e = 0
    tn_e = 0
    fn_e = 0
    for classified_as in classification_dict['entertainment']:
        if classified_as == 'entertainment':
            tp_e += 1
        else:
            fn_e += 1
    for classified_as in classification_dict['politics']:
        if classified_as == 'entertainment':
            fp_e += 1
    for classified_as in classification_dict['business']:
        if classified_as == 'entertainment':
            fp_e += 1
    tn_e = total_doc - (tp_e + fp_e + fn_e)   
    
    print "For entertainment:"
    print "~~~~~~"
    print "tp:" + str(tp_e)
    print "fp:" + str(fp_e)
    print "fn: " + str(fn_e)
    print "tn: " + str(tn_e)
    print "~~~~~~"

    
    tp = tp_p + tp_b + tp_e
    fp = fp_p + fp_b + fp_e
    fn = fn_p + fn_b + fn_e
    
    p = 1.0 * tp / (tp + fp)
    #print "Precision is " + str(p)
    r = 1.0 * tp / (tp +fn)
    #print "Recall is " + str(r)
    return (2*p*r / (p+r))

def Classification( doc, training_info, length ):
    stop_word_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','each','few','for','from','further','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself',"let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours' ]
    
    score = defaultdict(float)

    #Naive Bayes Classification Rule
    for category in training_info:
        smoothing_denomitor = length + training_info[category][ 'class_tokens' ]
        score[category] = math.log( training_info[category][ 'class_probability' ], 2 )
        
        for token in doc.lower().split():
            if token in training_info[category][ 'word_probability' ]:
                score[category] += math.log( training_info[category][ 'word_probability' ][ token ], 2 )
            else:
                if token in stop_word_list:
                    continue
                temp = 1.0  / smoothing_denomitor
                score[category] += math.log( temp, 2 )
    sorted_list = sorted(score.values(), reverse = True)
    for category in score:
        if score[ category ] == sorted_list[ 0 ]:
            return category


def TrainingSetLen( dict1, dict2, dict3 ):
    merge_dict = defaultdict( int )
    for word in dict1:
        merge_dict[ word ] += dict1[ word ]
    for word in dict2:
        merge_dict[ word ] += dict2[ word ]
    for word in dict3:
        merge_dict[ word ] += dict3[ word ]
    return len( merge_dict )
    
if __name__ == "__main__":
    main()
