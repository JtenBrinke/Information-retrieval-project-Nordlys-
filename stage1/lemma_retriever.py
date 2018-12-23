from pywsd.lesk import simple_lesk
import nltk

#Provides the sysnet (collection of words) that is synonymous to a given word, given its context.
def provide_synset(word, context):
    try:
        answer=simple_lesk(context, word, pos='n')
        return answer
    except IndexError:
        #print("PYWSD DOES NOT LIKE THIS WORD BECAUSE OF A BUG:")
        #print(word)
        return None

#Returns a list of all nouns in the query using postagging
def findNouns(query):
    tokenized = nltk.word_tokenize(query)
    allnouns=[]
    for (word, pos) in nltk.pos_tag(tokenized):
        if pos=='NN':
            allnouns.append(word)
    return allnouns

#Returns a limited set of synonyms that are different to the input noun.
def findUniqueSynonyms(noun,context,limit):
    found=[]
    if(provide_synset(noun, context) is None):
        return []    
        
    for lemma in provide_synset(noun, context).lemmas():
        foundterm=lemma.name().replace("_"," ")
        if foundterm!=noun:
            found.append(foundterm)
    return found[:limit]

#Returns the input query string with additional synonyms for the nouns (limit sets max. synonym limit per noun)
def addSynonymsToQuery(query, limit):
    #limit for maximum number of synonyms per noun

    allnouns = findNouns(query)
    allsynonyms = []
    for noun in allnouns:
        allsynonyms = allsynonyms + findUniqueSynonyms(noun,query,limit)

    newquery=query
    for word in allsynonyms:
        newquery=newquery+" "+word
    return newquery


# These things need to be manually entered into a python console if they have not yet been downloaded yet. Python does not parse these through this script for some weird reason.
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
