from collections import defaultdict
from pybing import Bing
import requests
import json
import FetchDoc

def main():
    my_key = 'XTQNxpp6Io9Qcl2DnZlzfJzM6sxksUIGV2XulHh8Z8w='
    params = {'$format' : 'json','$top' : 15,'$skip' : 0, 'NewsCategory': '' }
    query_num = 5
    query_category_doc_dict = defaultdict( lambda : defaultdict(list) )
    count = 0
    category = { 'entertainment':"'rt_Entertainment'", 'business':"'rt_Business'", 'politics':"'rt_Politics'" }

    #Obtain docs from Bing and write them to "docs.txt"
    #query_category_doc_dict has the following structure:
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
    f = open( 'TestDocs.json', 'w' )
    i = 0
    while i < query_num:
        my_query = raw_input( "Please input your query:" )
        bing = FetchDoc.BingSearchAPI( my_key )

        for cat in category:
            params[ 'NewsCategory' ] = category[cat]
            #obtain 30 documents for a query under a category
            j = 0
            while j < 30:
                params[ '$skip' ] = j
                search_request = bing.searchRequest( 'News', my_query, params )
                response = requests.get( search_request )
                Json_Dict = response.json()
                for my_dict in Json_Dict[ 'd' ][ 'results' ]:
                    count += 1
                    doc_content = my_dict[ 'Title' ] + " " + my_dict[ 'Description' ]
                    query_category_doc_dict[ my_query ][ cat ].append(doc_content)
                print "Retrieved Documents Number: " + str(count)
                j += 15
        i += 1
    f.write( json.dumps( query_category_doc_dict )+'\n' )
    
    print "A total number of " + str(count) + " documents are retrieved from Bing!"
    
    f.close()

if __name__ == "__main__":
    main()
