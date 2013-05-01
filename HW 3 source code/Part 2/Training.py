"""
The program is the training stage of Naive Bayes algorithm
"""

from collections import defaultdict
import json
import re
import sys

def main():
    #category_dict structure:{"politics":["...",...], "business":["...",...],"entertainment":["...",...]}
    f = open( "docs.json", "r" )
    category_dict = json.loads( f.readline().strip('\n') )
    f.close()
    
    training(category_dict)



def training( category_dict ):
    class_info = defaultdict( lambda : defaultdict() )
    
    politics_list = category_dict[ 'politics' ]
    business_list = category_dict[ 'business' ]
    entertainment_list = category_dict[ 'entertainment' ]
    total_doc_num = len(politics_list)+len(business_list)+len(entertainment_list)
    print total_doc_num

    #p_politics, p_business and p_entertainment are the prior probabilities of the three classes
    p_politics = 1.0 * len(politics_list) / total_doc_num
    p_business = 1.0 * len(business_list) / total_doc_num
    p_entertainment = 1.0 * len(entertainment_list) / total_doc_num


    politics_tf = ExtractVocabulary(politics_list)
    business_tf = ExtractVocabulary(business_list)
    entertainment_tf = ExtractVocabulary(entertainment_list)
    Training_Set_Vocabulary_len = TrainingSetLen( politics_tf, business_tf, entertainment_tf )
    
    POLITICS_TOKENS = Count(politics_tf)
    BUSINESS_TOKENS = Count(business_tf)
    ENTERTAINMENT_TOKENS = Count(entertainment_tf)

    politics_prob = CondProb(politics_tf, Training_Set_Vocabulary_len, POLITICS_TOKENS )
    business_prob = CondProb(business_tf, Training_Set_Vocabulary_len, BUSINESS_TOKENS )
    entertainment_prob = CondProb(entertainment_tf, Training_Set_Vocabulary_len, ENTERTAINMENT_TOKENS )

    class_info[ 'politics' ][ 'class_probability' ] = p_politics
    class_info[ 'politics' ][ 'word_probability' ] = politics_prob
    class_info[ 'politics' ][ 'class_tokens' ] = POLITICS_TOKENS
    
    class_info[ 'business' ][ 'class_probability' ] = p_business
    class_info[ 'business' ][ 'word_probability' ] = business_prob
    class_info[ 'business' ][ 'class_tokens' ] = BUSINESS_TOKENS
    
    class_info[ 'entertainment' ][ 'class_probability' ] = p_entertainment
    class_info[ 'entertainment' ][ 'word_probability' ] = entertainment_prob
    class_info[ 'entertainment' ][ 'class_tokens' ] = ENTERTAINMENT_TOKENS
    
    WriteToFile( class_info )

#Count counts the total number of tokens in politics(business,entertainment)
def Count( class_tf ):
    total_tokens = 0
    for word in class_tf:
        total_tokens += class_tf[ word ]
    return total_tokens

#TrainingSetLen counts the number of terms in the 150 retrieved documents
def TrainingSetLen( dict1, dict2, dict3 ):
    merge_dict = defaultdict( int )
    for word in dict1:
        merge_dict[ word ] += dict1[ word ]
    for word in dict2:
        merge_dict[ word ] += dict2[ word ]
    for word in dict3:
        merge_dict[ word ] += dict3[ word ]
    return len( merge_dict )


def WriteToFile( class_info ):
    f = open( "TrainingResult.json", 'w' )
    f.write( json.dumps(class_info) + '\n' )
    f.close()

#ExtractVocabulary counts how many times a term occurs politics(business, entertainment) documents
def ExtractVocabulary(class_list):
    stop_word_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','each','few','for','from','further','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself',"let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours' ]
    vacabulary_dict = defaultdict( int )
    for doc in class_list:
        for word in re.findall( r'[0-9a-z]+', doc.lower() ):
            if word in stop_word_list:
                continue
            vacabulary_dict[ word ] += 1
    return vacabulary_dict

#CondProb calculates conditional probabilities
#Given a class, what is the probability of the word apprearing in the class
def CondProb(class_tf, Training_Set_Vocabulary_len, class_tokens ):
    class_prob = defaultdict( float )
    denomitor = Training_Set_Vocabulary_len + class_tokens
    
    for word in class_tf:
        class_prob[ word ] = 1.0 * (1 + class_tf[ word ]) / denomitor
        
    return class_prob


if __name__ == "__main__":
    main()
