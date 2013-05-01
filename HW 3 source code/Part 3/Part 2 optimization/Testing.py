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

    h = open( "df.json", 'r' )
    df = json.loads( h.readline().strip( '\n' ) )
    h.close()

    i = open( "centroid.json", 'r' )
    centroid = json.loads( i.readline().strip( '\n' ) )
    i.close()
    
    Test( category_dict, training_info, df, centroid )

    
def Test( category_dict, training_info, df, centroid ):
    length = TrainingSetLen( training_info["politics"]["word_probability"], training_info["business"]["word_probability"], training_info["entertainment"]["word_probability"] )
    
    classification_dict = defaultdict( list )
    for my_query in category_dict:
        print "~~~~~~~~~~~~~~~~~~"
        print "Query:" + my_query
        for category in category_dict[ my_query ]:
            print "Search Category(Ground Truth):" + category
            category_list = category_dict[ my_query ][ category ]
            for doc in category_list:
                classified_as = Classification( doc, training_info, length, df, centroid )
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
    print "Precision is " + str(p)
    r = 1.0 * tp / (tp +fn)
    print "Recall is " + str(r)
    return (2*p*r / (p+r))

def Classification( doc, training_info, length, df, centroid ):
    stop_word_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','each','few','for','from','further','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself',"let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours' ]
    bi_word = ""
    tri_word = ""    
    score = defaultdict(float)

    #Naive Bayes Classification Rule
    for category in training_info:
        smoothing_denomitor = length + training_info[category][ 'class_tokens' ]
        score[category] = math.log( training_info[category][ 'class_probability' ], 2 )
        
        for token in doc.lower().split():
            bi_word += token + " "
            tri_word += token + " "

            if token in training_info[category][ 'word_probability' ]:
                score[category] += math.log( training_info[category][ 'word_probability' ][ token ], 2 )
            else:
                if token in stop_word_list:
                    continue
                temp = 1.0  / smoothing_denomitor
                score[category] += math.log( temp, 2 )

            if len(bi_word.split()) == 2:
                if bi_word in training_info[category][ 'word_probability' ]:
                    score[category] += math.log( training_info[category][ 'word_probability' ][ bi_word ], 2 )
                bi_word = bi_word.split()[1] + " "
                

            if len(tri_word.split()) == 3:
                if tri_word in training_info[category][ 'word_probability' ]:
                    score[category] += math.log( training_info[category][ 'word_probability' ][ tri_word ], 2 )
                tri_word = tri_word.split()[1] + " " + tri_word.split()[2] + " "

    NB_Result = defaultdict()
    sorted_list = sorted(score.values(), reverse = True)
    for category in score:
        if score[ category ] == sorted_list[ 0 ]:
            NB_Result[0] = category
        elif score[ category ] == sorted_list[ 1 ]:
            NB_Result[1] = category
        else:
            NB_Result[2] = category

    #Rocchio Classification Rule
    doc_tf = defaultdict(float)
    for token in doc.lower().split():
        if token in stop_word_list:
            continue
        if df.has_key(token):
            doc_tf[token] += 1
            
    for term in df:
        if doc_tf.has_key(term):
            doc_tf[term] = (1 + math.log(doc_tf[term],2)) * math.log(1335.0/df[term],2)
        else:
            doc_tf[term] = 0
    Rocchio_Result = Rocchio_Cosine( doc_tf, centroid )
    
    combined_score = defaultdict(int)
    combined_score[ NB_Result[0] ] += 0
    combined_score[ NB_Result[1] ] += 1
    combined_score[ NB_Result[2] ] += 2
    combined_score[ Rocchio_Result[0] ] += 0
    combined_score[ Rocchio_Result[1] ] += 1
    combined_score[ Rocchio_Result[2] ] += 2

    sorted_combined_score = sorted(combined_score.values())
    val = sorted_combined_score[0]
    for cate in combined_score:
        if combined_score[cate] == val:
            return cate
        

def Rocchio_Cosine( doc_tf, centroid ):
    denominator = 0
    p_val_nominator = 0
    b_val_nominator = 0
    e_val_nominator = 0

    p_denominator = 0
    b_denominator = 0
    e_denominator = 0

    
    for term in doc_tf:
        p_val_nominator += doc_tf[term] * centroid["politics"][term]
        b_val_nominator += doc_tf[term] * centroid["business"][term]
        e_val_nominator += doc_tf[term] * centroid["entertainment"][term]

        denominator += math.pow( doc_tf[term],2 )
        p_denominator += math.pow( centroid["politics"][term],2 )
        b_denominator += math.pow( centroid["business"][term],2 )
        e_denominator += math.pow( centroid["entertainment"][term],2 )

    p = 1.0 * p_val_nominator /( math.sqrt(denominator) * math.sqrt( p_denominator ) )
    b = 1.0 * b_val_nominator /( math.sqrt(denominator) * math.sqrt( b_denominator ) )
    e = 1.0 * e_val_nominator /( math.sqrt(denominator) * math.sqrt( e_denominator ) )
    Rocchio_Dict = defaultdict(float)
    Rocchio_Dict["politics"] = p
    Rocchio_Dict["business"] = b
    Rocchio_Dict["entertainment"] = e

    Result_List = sorted(Rocchio_Dict.values(), reverse = True)
    Result_Dict = defaultdict()
    i = 0
    while i < len(Result_List):
        for key in Rocchio_Dict:
            if Rocchio_Dict[key] == Result_List[i]:
                Result_Dict[i] = key
        i += 1
        
    return Result_Dict

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
