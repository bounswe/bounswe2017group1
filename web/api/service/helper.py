
import requests

#This code uses Datamuse API
def get_concepts_from_item(source):
    source = source.lower()
    myList = []
    obj = requests.get('https://api.datamuse.com/words?ml='+source.replace(" ", "+")).json()
    for data in obj:
        myList.append((data['word'], data['score']))
        if len(myList)>9:
            break
    return myList

def get_concepts_from_list(source):
    myList = []
    for entry in source:
        entry = entry.lower()
        obj = requests.get('https://api.datamuse.com/words?ml='+entry.replace(" ", "+")).json()
        for data in obj:
            if data['word'] in [x[0] for x in myList]:
                index = [x[0] for x in myList].index(data['word'])
                myList[index] = (myList[index][0], myList[index][1]+data['score'])
            else:
                myList.append((data['word'], data['score']))

    myList.sort(key=lambda tup: tup[1], reverse=True);

    myList = myList[:10]
    return myList


"""
#Code that uses ConceptNet API

def get_concepts_from_item(source):
    source = source.lower();
    print source;
    myList = [];
    obj = requests.get('http://api.conceptnet.io/c/en/'+source.replace(" ", "_")).json();
    for edge in obj['edges']:
        weight = edge['weight'];
        if source not in edge['start']['label'].lower() and edge['start']['language'] == "en":
            word = edge['start']['label'].lower();
            myList.append((word, weight));
        elif source not in edge['end']['label'].lower() and edge['end']['language'] == "en":
            word = edge['end']['label'].lower();
            myList.append((word, weight));

        if len(myList)>9 and myList[len(myList)-1][1] < 4:
            break;

    return myList;


def get_concepts_from_list(source):
    myList = [];
    for entry in source:
        entry = entry.lower();
        print entry
        obj = requests.get('http://api.conceptnet.io/c/en/'+entry.replace(" ", "_")).json();
        for edge in obj['edges']:

            weight = edge['weight'];
            if entry not in edge['start']['label'].lower() and edge['start']['language'] == "en":
                word = edge['start']['label'].lower();
                if word in [x[0] for x in myList]:
                    index = [x[0] for x in myList].index(word)
                    myList[index] = (myList[index][0], myList[index][1]+weight);
                else:
                    myList.append((word, weight));
            elif entry not in edge['end']['label'].lower() and edge['start']['language'] == "en":
                word = edge['end']['label'].lower();
                if word in [x[0] for x in myList]:
                    index = [x[0] for x in myList].index(word)
                    myList[index] = (myList[index][0], myList[index][1] + weight);
                else:
                    myList.append((word, weight));

    myList.sort(key=lambda tup: tup[1], reverse=True);

    for i in range(10,len(myList)):
        if myList[i][1] <4 :
            myList = myList[:i]
            break;

    return myList;
"""

"""
#Testing Area

word1 = "metropolis"
word2 = "Urban Center"
print word1, word2

#test = get_concepts_from_item(word1);
test = get_concepts_from_list([word1, word2]);

print len(test)
for p in test:
    print p

"""