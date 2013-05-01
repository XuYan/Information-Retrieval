"""
Usage:
	$python apriori.py

"""

import sys
import re
import json

from itertools	 import chain, combinations
from collections import defaultdict
from optparse 	 import OptionParser

def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
	"""calculates the support for items in the itemSet and returns a subset of the itemSet 
	each of whose elements satisfies the minimum support"""
	_itemSet = set()
	localSet = defaultdict(int)

	for item in itemSet:
		for transaction in transactionList:
			if item.issubset(transaction):
				freqSet[item] 	+= 1
				localSet[item]	+= 1
	
	for item,count in localSet.items():
		support = float(count)/len(transactionList)
		
		if support >= minSupport:
			_itemSet.add(item)
	
	return _itemSet



def joinSet(itemSet,length):
	"""Join a set with itself and returns the n-element itemsets"""
	return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    transactionList	= list()
    itemSet		= set()
    for record in data_iterator:
        #print record
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))		# Generate 1-itemSets
    return itemSet, transactionList


def runApriori(data_iter, minSupport, minConfidence):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both: 
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)
    
    freqSet		= defaultdict(int)
    largeSet		= dict()				# Global dictionary which stores (key=n-itemSets,value=support) which satisfy minSupport
    assocRules 		= dict()				# Dictionary which stores Association Rules
    
    oneCSet		= returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet)
    
    currentLSet	= oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] 	= currentLSet
        currentLSet 	= joinSet(currentLSet,k)
        currentCSet 	= returnItemsWithMinSupport(currentLSet, transactionList, minSupport, freqSet)
        currentLSet 	= currentCSet
        k = k + 1

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems=[]
    for key,value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item)) 
                           for item in value])

    toRetRules=[]
    for key,value in largeSet.items()[1:]:
        for item in value:
            _subsets = map(frozenset,[x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain)>0:
                    confidence = getSupport(item)/getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element),tuple(remain)), 
                                           confidence))
    return toRetItems, toRetRules


def printItemToItemResults(items, rules):
    """prints the generated itemsets and the confidence rules"""
    #for item, support in items:
        #print "item: %s , %.3f" % (str(item), support)
    #print "\n------------------------ RULES:"
    n = 0
    ruleList = []
    for rule, confidence in rules:
        pre, post = rule
        preSet = set()
        postSet = set()
        preConcatString = ''
        for item in pre:
            preConcatString = preConcatString + item.replace('[', '').replace(']', '')
            preSet.add(item.replace('[', '').replace(']', ''))
        postConcatString = ''
        for item in post:
            postConcatString = postConcatString + item.replace('[', '').replace(']', '')
            postSet.add(item.replace('[', '').replace(']', ''))
        if '5_' in preConcatString and '5_' in postConcatString:
            n = n + 1
            #print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
            wholeSet = set()
            wholeSet = preSet.union(postSet)
            if wholeSet not in ruleList:
                ruleList.append(wholeSet)
            #print wholeSet
    #print n
    print "after merging"
    returnList = []
    for x in range(len(ruleList)):
        if x < len(ruleList) - 1:
            y = x + 1
        else:
            y = x
        currRule = ruleList[x]
        isSubset = False
        while not isSubset:
            nextRule = ruleList[y]
            if currRule.issubset(nextRule):
                isSubset = True
            y = y + 1
            if y == len(ruleList):
                break
        if not isSubset:
            returnList.append(currRule)
    returnList.append(ruleList[-1])
    skillToSkillList = []
    for element in returnList:
        skillToSkillList.append(list(element))
    print len(skillToSkillList)
    return skillToSkillList

def printSkillToSkillResults(items, rules):
    """prints the generated itemsets and the confidence rules"""
    #for item, support in items:
        #print "item: %s , %.3f" % (str(item), support)
    #print "\n------------------------ RULES:"
    n = 0
    ruleList = []
    for rule, confidence in rules:
        pre, post = rule
        preSet = set()
        postSet = set()
        preConcatString = ''
        for item in pre:
            preConcatString = preConcatString + item.replace('[', '').replace(']', '')
            preSet.add(item.replace('[', '').replace(']', ''))
        postConcatString = ''
        for item in post:
            postConcatString = postConcatString + item.replace('[', '').replace(']', '')
            postSet.add(item.replace('[', '').replace(']', ''))
        if '1_' in preConcatString and '2_' in preConcatString and '1_' in postConcatString and '2_' in postConcatString:
            n = n + 1
            #print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
            wholeSet = set()
            wholeSet = preSet.union(postSet)
            if wholeSet not in ruleList:
                ruleList.append(wholeSet)
            #print wholeSet
    #print n
    returnList = []    
    print "after merging"
    for x in range(len(ruleList)):
        if x < len(ruleList) - 1:
            y = x + 1
        else:
            y = x
        currRule = ruleList[x]
        isSubset = False
        while not isSubset:
            nextRule = ruleList[y]
            if currRule.issubset(nextRule):
                isSubset = True
            y = y + 1
            if y == len(ruleList):
                break
        if not isSubset:
            returnList.append(currRule)
    if len(ruleList) != 0:
        returnList.append(ruleList[-1])
    skillToSkillList = []
    for element in returnList:
        skillToSkillList.append(list(element))
    print len(skillToSkillList)
    return skillToSkillList

def printSkillToRuneResults(items, rules):
    """prints the generated itemsets and the confidence rules"""
    #for item, support in items:
        #print "item: %s , %.3f" % (str(item), support)
    #print "\n------------------------ RULES:"
    n = 0
    ruleList = []
    for rule, confidence in rules:
        pre, post = rule
        preSet = set()
        postSet = set()
        preConcatString = ''
        for item in pre:
            preConcatString = preConcatString + item.replace('[', '').replace(']', '')
            preSet.add(item.replace('[', '').replace(']', ''))
        postConcatString = ''
        for item in post:
            postConcatString = postConcatString + item.replace('[', '').replace(']', '')
            postSet.add(item.replace('[', '').replace(']', ''))
        if '1_' in preConcatString and '2_' in preConcatString and '3_' in postConcatString:
            n = n + 1
            print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
            wholeSet = set()
            wholeSet = preSet.union(postSet)
            if wholeSet not in ruleList:
                ruleList.append(wholeSet)
            #print wholeSet
    #print n
    print len(ruleList)
    for rule in ruleList:
        print rule
    returnList = []
    print "after merging"
    for x in range(len(ruleList)):
        if x < len(ruleList) - 1:
            y = x + 1
        else:
            y = x
        currRule = ruleList[x]
        isSubset = False
        while not isSubset:
            nextRule = ruleList[y]
            if currRule.issubset(nextRule):
                isSubset = True
            y = y + 1
            if y == len(ruleList):
                break
        if not isSubset:
            returnList.append(currRule)
    returnList.append(ruleList[-1])
    skillToSkillList = []
    for element in returnList:
        skillToSkillList.append(list(element))
    print len(skillToSkillList)
    return skillToSkillList

    
def printSkillToItemResults(items, rules):
    """prints the generated itemsets and the confidence rules"""
    #for item, support in items:
        #print "item: %s , %.3f" % (str(item), support)
    #print "\n------------------------ RULES:"
    n = 0
    ruleList = []
    for rule, confidence in rules:
        pre, post = rule
        preSet = set()
        postSet = set()
        preConcatString = ''
        for item in pre:
            preConcatString = preConcatString + item.replace('[', '').replace(']', '')
            preSet.add(item.replace('[', '').replace(']', ''))
        postConcatString = ''
        for item in post:
            postConcatString = postConcatString + item.replace('[', '').replace(']', '')
            postSet.add(item.replace('[', '').replace(']', ''))
        if '1_' in preConcatString and '2_' in preConcatString and '5_' in postConcatString:
            n = n + 1
            #print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
            wholeSet = set()
            wholeSet = preSet.union(postSet)
            if wholeSet not in ruleList:
                ruleList.append(wholeSet)
            #print wholeSet
    #print n
    print len(ruleList)
    for rule in ruleList:
        print rule
    returnList = []
    print "after merging"
    for x in range(len(ruleList)):
        if x < len(ruleList) - 1:
            y = x + 1
        else:
            y = x
        currRule = ruleList[x]
        isSubset = False
        while not isSubset:
            nextRule = ruleList[y]
            if currRule.issubset(nextRule):
                isSubset = True
            y = y + 1
            if y == len(ruleList):
                break
        if not isSubset:
            returnList.append(currRule)
    returnList.append(ruleList[-1])
    skillToSkillList = []
    for element in returnList:
        skillToSkillList.append(list(element))
    print len(skillToSkillList)
    return skillToSkillList

def dataFromFile(fname):
	"""Function which reads from the file and yields a generator"""
	file_iter = open(fname, 'rU')
   	for line in file_iter:
		line = line.strip().rstrip(',')				# Remove trailing comma
		record = frozenset(line.split(','))
		yield record

def getAssociated(items, rules):
    associatedTerms = []
    for rule, confidence in rules:
        associatedTerm = []
        pre, post = rule
        for item in pre:
            associatedTerm.append(item.replace('[', '').replace(']', '').lstrip().replace('\'', ''))
            #print item.replace('[', '').replace(']', '')
        for item in post:
            associatedTerm.append(item.replace('[', '').replace(']', '').lstrip().replace('\'', ''))
            #print item.replace('[', '').replace(']', '')
        associatedTerm = set(associatedTerm)
        associatedTerms.append(associatedTerm)
    return associatedTerms

if __name__ == "__main__":
    '''
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile', dest = 'input', help = 'the filename which contains the comma separated values', default=None)
    optparser.add_option('-s', '--minSupport', dest='minS', help = 'minimum support value', default=0.15, type='float')
    optparser.add_option('-c','--minConfidence', dest='minC', help = 'minimum confidence value', default = 0.6, type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
	    inFile = sys.stdin
    elif options.input is not None:
	    inFile = dataFromFile(options.input)
    else:
	    print 'No dataset filename specified, system with exit\n'
	    sys.exit('System will exit')
    '''

    ''' 1_: active skills
        2_: passive skills
        3_: runes with active skills
        4_: runes with passive skills
        5_: items
    '''
    #inFile = dataFromFile('wizard.csv')
    '''
    print "Item to Item"
    inFile = dataFromFile('wizard.csv')
    minSupport		= 0.04 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    itemToItem = {}
    itemToItem['ItemToItem'] = printItemToItemResults(items, rules)
    with open('wizard.json', 'a') as outfile:
        json.dump(itemToItem, outfile)
        outfile.write('\n')
    outfile.close()    
    
    print "Skill to Skill"
    minSupport		= 0.05 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToSkill = {}
    skillToSkill['SkillToSkill'] = printSkillToSkillResults(items, rules)
    with open('wizard.json', 'a') as outfile:
        json.dump(skillToSkill, outfile)
        outfile.write('\n')
    outfile.close()
    
    print "Skill to Rune"
    minSupport		= 0.09 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToRune = {}
    skillToRune['SkillToRune'] = printSkillToRuneResults(items, rules)
    with open('wizard.json', 'a') as outfile:
        json.dump(skillToRune, outfile)
        outfile.write('\n')
    outfile.close()
    
    
    print "Skill to Item"
    minSupport		= 0.035 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToItem = {}
    skillToItem['SkillToItem'] = printSkillToItemResults(items, rules)
    with open('wizard.json', 'a') as outfile:
        json.dump(skillToItem, outfile)
        outfile.write('\n')
    outfile.close()
    '''
    
    
    
    '''
    print "Item to Item"
    minSupport		= 0.035 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    itemToItem = {}
    itemToItem['ItemToItem'] = printItemToItemResults(items, rules)
    with open('demon-hunter.json', 'a') as outfile:
        json.dump(itemToItem, outfile)
        outfile.write('\n')
    outfile.close()    
    
    print "Skill to Skill"
    minSupport		= 0.12 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToSkill = {}
    skillToSkill['SkillToSkill'] = printSkillToSkillResults(items, rules)
    with open('demon-hunter.json', 'a') as outfile:
        json.dump(skillToSkill, outfile)
        outfile.write('\n')
    outfile.close()
    
    print "Skill to Rune"
    minSupport		= 0.09 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToRune = {}
    skillToRune['SkillToRune'] = printSkillToRuneResults(items, rules)
    with open('demon-hunter.json', 'a') as outfile:
        json.dump(skillToRune, outfile)
        outfile.write('\n')
    outfile.close()
    
    
    print "Skill to Item"
    minSupport		= 0.03 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToItem = {}
    skillToItem['SkillToItem'] = printSkillToItemResults(items, rules)
    with open('demon-hunter.json', 'a') as outfile:
        json.dump(skillToItem, outfile)
        outfile.write('\n')
    outfile.close()
    '''
    #inFile = dataFromFile('monk.csv')
    '''
    print "Item to Item"
    minSupport		= 0.0253 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    itemToItem = {}
    itemToItem['ItemToItem'] = printItemToItemResults(items, rules)
    with open('monk.json', 'a') as outfile:
        json.dump(itemToItem, outfile)
        outfile.write('\n')
    outfile.close()    
    
    print "Skill to Skill"
    minSupport		= 0.05 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToSkill = {}
    skillToSkill['SkillToSkill'] = printSkillToSkillResults(items, rules)
    with open('monk.json', 'a') as outfile:
        json.dump(skillToSkill, outfile)
        outfile.write('\n')
    outfile.close()
    
    print "Skill to Rune"
    minSupport		= 0.11 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToRune = {}
    skillToRune['SkillToRune'] = printSkillToRuneResults(items, rules)
    with open('monk.json', 'a') as outfile:
        json.dump(skillToRune, outfile)
        outfile.write('\n')
    outfile.close()
    
    
    print "Skill to Item"
    minSupport		= 0.025 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToItem = {}
    skillToItem['SkillToItem'] = printSkillToItemResults(items, rules)
    with open('monk.json', 'a') as outfile:
        json.dump(skillToItem, outfile)
        outfile.write('\n')
    outfile.close()
    '''
    inFile = dataFromFile('barbarian.csv')
    '''
    print "Item to Item"
    minSupport		= 0.1 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    itemToItem = {}
    itemToItem['ItemToItem'] = printItemToItemResults(items, rules)
    with open('barbarian.json', 'a') as outfile:
        json.dump(itemToItem, outfile)
        outfile.write('\n')
    outfile.close()    
    
    print "Skill to Skill"
    minSupport		= 0.17 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToSkill = {}
    skillToSkill['SkillToSkill'] = printSkillToSkillResults(items, rules)
    with open('barbarian.json', 'a') as outfile:
        json.dump(skillToSkill, outfile)
        outfile.write('\n')
    outfile.close()
    
    print "Skill to Rune"
    minSupport		= 0.18 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToRune = {}
    skillToRune['SkillToRune'] = printSkillToRuneResults(items, rules)
    with open('barbarian.json', 'a') as outfile:
        json.dump(skillToRune, outfile)
        outfile.write('\n')
    outfile.close()
    '''
    
    print "Skill to Item"
    minSupport		= 0.05 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToItem = {}
    skillToItem['SkillToItem'] = printSkillToItemResults(items, rules)
    with open('barbarian.json', 'a') as outfile:
        json.dump(skillToItem, outfile)
        outfile.write('\n')
    outfile.close()
    
    
    #inFile = dataFromFile('witch-doctor.csv')
    '''
    print "Item to Item"
    minSupport		= 0.02 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    itemToItem = {}
    itemToItem['ItemToItem'] = printItemToItemResults(items, rules)
    with open('witch-doctor.json', 'a') as outfile:
        json.dump(itemToItem, outfile)
        outfile.write('\n')
    outfile.close()    
    
    print "Skill to Skill"
    minSupport		= 0.04 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToSkill = {}
    skillToSkill['SkillToSkill'] = printSkillToSkillResults(items, rules)
    with open('witch-doctor.json', 'a') as outfile:
        json.dump(skillToSkill, outfile)
        outfile.write('\n')
    outfile.close()
    
    print "Skill to Rune"
    minSupport		= 0.07 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToRune = {}
    skillToRune['SkillToRune'] = printSkillToRuneResults(items, rules)
    with open('witch-doctor.json', 'a') as outfile:
        json.dump(skillToRune, outfile)
        outfile.write('\n')
    outfile.close()
    
    
    print "Skill to Item"
    minSupport		= 0.02 #options.minS
    minConfidence 	= 0.9 #options.minC
    items, rules	= runApriori(inFile, minSupport, minConfidence)
    skillToItem = {}
    skillToItem['SkillToItem'] = printSkillToItemResults(items, rules)
    with open('witch-doctor.json', 'a') as outfile:
        json.dump(skillToItem, outfile)
        outfile.write('\n')
    outfile.close()
    '''
    
    