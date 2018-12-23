import requests
import json

# Processes a list of queries and returns the list of json-responses
def processQueries(qlist):
    responses=[]
    for query in qlist:
        resp=requests.get(buildNordlysURL(query))
        if(resp.status_code != 200):
               print("Error while processing the following query:")
               print(query)
               print("Status code:")
               print(resp.status_code)
               raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        else:
            responses.append(resp.json())
    return responses

# Exports a list of json objects to a json file:
def exportJsonResults(jsons, filename):
    with open(filename, 'w') as f:
        for item in jsons:
            json.dump(item, f)
            f.write('\n')

# Imports a list of json objects from a json file:        
def importJsonResults(filename):
    imported=[]
    with open(filename, 'r') as f:
        for line in f:
            imported.append(json.loads(line))
    return imported

# Prints json object pretty
def pleasePrintJsonPretty(jsonresponse):
    #parsed = json.loads(jsonresponse)
    dinges = json.dumps(jsonresponse, indent=4,sort_keys=True)
    print dinges


# Builds nordlys url given parameters
def buildNordlysURL(q):
    initialStr = "http://api.nordlys.cc/"
    derest = "er?q="
    outputStr=initialStr+derest+q.replace(" ","+")
    print(outputStr)
    return outputStr


