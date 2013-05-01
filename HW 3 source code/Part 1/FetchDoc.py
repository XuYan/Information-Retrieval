from pybing import Bing
from collections import defaultdict
import requests
import json
import string

class BingSearchAPI():
    url1 = "https://user:"
    url2 = "@api.datamarket.azure.com/Bing/Search/"
    
    def __init__(self, key):
        self.key = key

    def replace_symbols(self, request):
        request = string.replace(request, "'", '%27')
        request = string.replace(request, '"', '%27')
        request = string.replace(request, '+', '%2b')
        request = string.replace(request, ' ', '%20')
        request = string.replace(request, ':', '%3a')
        return request
        
    def searchRequest(self, sources, query, params):
        request = sources + "?Query='" + query + "'"
        for key,value in params.iteritems():
            request += '&' + key + '=' + str(value)
            
        request = self.replace_symbols(request)
        request = self.url1 + self.key + self.url2 + request

        return request


if __name__ == "__main__":
    my_key = 'XTQNxpp6Io9Qcl2DnZlzfJzM6sxksUIGV2XulHh8Z8w='
    params = {'$format' : 'json','$top' : 15,'$skip' : 0 }
    query_num = 5
    Doc = defaultdict()
    Query_Title_Pair = defaultdict(list)
    count = 0

    #Obtain docs from Bing and write them to "docs.txt"
    f = open( 'docs.json', 'w' )
    #Record {query:[titles]} for purity calculation later
    g = open( 'title.json', 'w' )
    i = 0
    while i < query_num:
        my_query = raw_input( "Please input your query:" )
        bing = BingSearchAPI( my_key )
        j = 0
        while j < 30:
            params[ '$skip' ] = j
            search_request = bing.searchRequest( 'News', my_query, params )
            response = requests.get( search_request )
            Json_Dict = response.json()

            for my_dict in Json_Dict[ 'd' ][ 'results' ]:
                count += 1
                Doc[ 'title' ] = my_dict[ 'Title' ]
                Doc[ 'description' ] = my_dict[ 'Description' ]
                Query_Title_Pair[ my_query ].append( my_dict[ 'Title' ] )
                f.write( json.dumps( Doc )+'\n' )
                
            j += 15
        i += 1
        print my_query + ": " + str( count ) + " documents are retrieved!"
    g.write( json.dumps( Query_Title_Pair ) )
    print str(count) + " documents are retrieved from Bing!"
    g.close()
    f.close()
    
