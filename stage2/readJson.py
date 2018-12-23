# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:28:37 2018

"""

##NOTE: this is a python 3 script, in contrast to stage 1.

import json
import numpy as np
import math

def importJsonResults(filename):
    imported = []
    with open(filename, 'r') as f:
        for line in f:
            imported.append(json.loads(line))
    return imported
    
#resp = importJsonResults('json_export_origquerylist.json') #original queries
#resp = importJsonResults('json_export_newquerylist_1syn.json') #expanded queries, 1 syn
resp = importJsonResults('json_export_newquerylist_2syn.json') #expanded queries, 2 syns

#To get the query codes
queries = list(open("queries-v2.txt", "r"))
querycodes = []
for q in queries:
    qs = q.split("\t")
    querycodes.append(qs[0])

#to get the relevant queries, with their dbpedia page and relevance score
#[code, something, dbpedia page, relevance score]
qrels = list(open("qrels-v2.txt", "r"))
qrelsplit = []
for q in qrels:
    qs = q.split("\t")
    qrelsplit.append(qs)

averagePs = []
NDCGs = []
recalls = []
foundrelevants = []
for j in range (0,len(resp)-1): #for all queries (so length of response list) 
    precisions = []    
    entities = []
    querycode = querycodes[j] #we assume the lists are in the same order lol
    rels = []
    
    #only add relevance shit if the querycode is the same lol
    relevantqrels = 0
    for qr in qrelsplit:
        if(querycode == qr[0]):
            rels.append(qr)
            if(int(qr[3])>0):
                relevantqrels += 1
    
    relevantentries = []
    for i in range (0,len(resp[j]["results"])-1): #for all responses of query j (so for MAP)
    #for i in range (0, (min(10,(len(resp[j]["results"])-1)))): # only top 10 results 
        entities.append(resp[j]["results"][str(i)]["entity"])
        for r in rels:
            relscore = 0
            if (entities[i] == str(r[2])):
                relscore = int(r[3])
            if relscore > 0: 
                relevantentries.append([entities[i], relscore, i])
    
    foundrelevants.append(len(relevantentries))
    recalls.append(len(relevantentries)/relevantqrels)
    
    if(len(relevantentries)>0):
        sortedRE = np.sort(relevantentries, axis=1)
        DCG = 0
        IDCG = 0
        NDCG = 0
        for k in range (0, (min(10, len(relevantentries)))): #voor NDCG@10? only top 10 results
            DCG = DCG + (int(relevantentries[k][1])/float(math.log2(k+2)))
            IDCG = IDCG + (int(sortedRE[k][1])/float(math.log2(k+2)))
        NDCG = DCG/IDCG
        NDCGs.append(NDCG)
    
                
    #calculate precision with the relevantentries list
    for l in range (0,(len(relevantentries)-1)):
        p = float(float(l+1)/float(relevantentries[l][2]+1))
        precisions.append(p)
        
    #sometimes it goes wrong?? p is calculated but somehow not added to precisions?
    #so add it manually lol
    if(len(precisions) == 0):
        precisions.append(p)
    averageP = float(np.average(precisions))
    averagePs.append(averageP)

meanAP = np.average(averagePs) #voor alle queries
print('MAP = ', meanAP)
meanNDCG = np.average(NDCGs)
print('NDCG@10 = ', meanNDCG)
meanRecall = np.average(recalls)
print('Recall = ', meanRecall)

        
#WITH ORIGINAL QUERIES:
### MAP = 0.426124765113
### NDCG@10 = 0.200992584813
### Recall = 0.718190259442
        
#WITH 1-syn QUERIES:
### MAP = 0.378447471143
### NDCG@10 = 0.181100935591
### Recall =  0.702082657889

#With 2-syn QUERIES:
###MAP =  0.34316872325
###NDCG@10 =  0.164559873375
###Recall =  0.690245910945

#With 3-syn QUERIES:
# Nordlys is down :(
