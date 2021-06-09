import json
import random
Type=json.load(open('typefinder.json','r'))
def filltype(ex):
    existing=[]
    key=""
    for x in range (0,10):
        key=key+str(random.randint(0,9))
    Type=json.load(open('typefinder.json','r'))
    Type[key]=[]
    ex=ex.replace("?","")
    ex=ex.replace("!","")
    ex=ex.replace("#","")
    ex=ex.replace("$","")
    ex=ex.replace("@","")
    ex=ex.replace("%","")
    ex=ex.replace("*","")
    ex=ex.replace("&","")
    ex=ex.replace("/","")
    ex=ex.lower()
    ex=ex.split()
    for words in ex:
        if(words in existing):
            pass
        else:
            Type[key].append(words)
            existing.append(words)
    json.dump(Type,open('typefinder.json','w'))
    return(key)