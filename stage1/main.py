import lemma_retriever
import nordlys_comms
import csv

databaselist=[] # This list contains the first column of the dataset; the ones that start with "INEX", etc.
origquerylist=[] # The unmodified queries from the dataset
newquerylist=[] # The modified queries that have added synonyms


# Load query database:
with open('queries-v2.txt', 'r') as f:
    for line in f:
        #print line.strip().split("\t")
        databaselist.append(line.strip().split("\t")[0])
        origquerylist.append(line.strip().split("\t")[1])

# Create queries with added synonyms for nouns, in this case a maximum of 3 terms are added per noun:
for query in origquerylist:
    newquery=lemma_retriever.addSynonymsToQuery(query, 3)
    newquerylist.append(newquery)

# Create list of responses through Nordlys:
testResponses= nordlys_comms.processQueries(newquerylist)

# Export the responses to a file:
nordlys_comms.exportJsonResults(testResponses, 'json_export_newquerylist_3syn.json')

# If you wish to reimport:
#importedResponses=nordlys_comms.importJsonResults('json_export.json')

print("done!")


## Useful if you want to create an overview of the modified vs. unmodified queries:
# Save the results to file (tab-separated):
#print("Exporting results")
#with open('output.txt', 'w') as f:
#    i=0
#    while(i<len(databaselist)):
#        f.write(databaselist[i] + "\t" + origquerylist[i] + "\t" + newquerylist[i] + "\t" + origQueryResponses + #"\t" + newQueryResponses + "\n")
#        i+=1

# Render Arjen:
import arj
