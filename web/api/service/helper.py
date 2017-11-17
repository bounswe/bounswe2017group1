
import requests



def get_concepts_from_item(source):
    source = source.lower();
    myList = [];
    obj = requests.get('http://api.conceptnet.io/c/en/'+source).json();
    for edge in obj['edges']:
        weight = edge['weight'];
        if source not in edge['start']['label'].lower():
            word = edge['start']['label'];
            myList.append((word, weight));
        elif source not in edge['end']['label'].lower():
            word = edge['end']['label'];
            myList.append((word, weight));

    return myList;


def get_concepts_from_list(source):
    myList = [];
    for entry in source:
        entry = entry.lower();
        obj = requests.get('http://api.conceptnet.io/c/en/'+entry).json();
        for edge in obj['edges']:
            weight = edge['weight'];
            if entry not in edge['start']['label'].lower():
                word = edge['start']['label'].lower();
                if word in [x[0] for x in myList]:
                    index = [x[0] for x in myList].index(word)
                    myList[index] = (myList[index][0], myList[index][1]+weight);
                else:
                    myList.append((word, weight));
            elif entry not in edge['end']['label'].lower():
                word = edge['end']['label'].lower();
                if word in [x[0] for x in myList]:
                    index = [x[0] for x in myList].index(word)
                    myList[index] = (myList[index][0], myList[index][1] + weight);
                else:
                    myList.append((word, weight));

    myList.sort(key=lambda tup: tup[1], reverse=True);
    return myList;



        


"""

#test = get_concepts_from_item('football');
test = get_concepts_from_list(['sport', 'football']);

print len(test)
for p in test:
    print p
    

"""