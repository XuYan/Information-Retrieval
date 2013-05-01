"""
The ultimate goal of FetchDoc.py is to write category_doc_dict to file "docs.json"
category_doc_dict is a dictionary that has the following format:
{
'Politics':[document1_content,document2_content,document3_content,...]
'Business':
'Entertainment':
}
document_content is a string combining document title and document description.
Ideally speaking, the sum of the number of documents in "Politics","Business" and "Entertainment" should be 1350
"""
from pybing import Bing
from collections import defaultdict
import requests
import json
import string
import sys

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
    params = {'$format' : 'json','$top' : 1,'$skip' : 0, 'NewsCategory': '' }
    query_num = 3
    category_doc_dict = defaultdict( list )
    count = 0
    category = { 'entertainment':"'rt_Entertainment'", 'business':"'rt_Business'", 'politics':"'rt_Politics'" }

    #Obtain docs from Bing and write them to "docs.txt"
    f = open( 'docs.json', 'w' )
    i = 0
    while i < query_num:
        my_query = raw_input( "Please input your query:" )
        bing = BingSearchAPI( my_key )

        for cat in category:
            params[ 'NewsCategory' ] = category[cat]
            print cat
            #obtain 30 documents for a query under a category
            j = 0
            while j < 15:
                params[ '$skip' ] = j
                search_request = bing.searchRequest( 'News', my_query, params )
                response = requests.get( search_request )
                Json_Dict = response.json()
                for my_dict in Json_Dict[ 'd' ][ 'results' ]:
                    count += 1
                    doc_content = my_dict[ 'Title' ]
                    category_doc_dict[ cat ].append( doc_content )
                print "Retrieved Documents Number: " + str(count)
                j += 15
        i += 1
    f.write( json.dumps( category_doc_dict )+'\n' )
    
    print "A total number of " + str(count) + " documents are retrieved from Bing!"
    
    f.close()
