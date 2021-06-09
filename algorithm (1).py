import json
import random
def AI(inputgiven):
    dataset=json.load(open('typefinder.json','r'))
    responses=json.load(open('responses.json','r'))
    inputwords=inputgiven.lower()
    inputwords=inputwords.replace("?","")
    inputwords=inputwords.replace("!","")
    inputwords=inputwords.replace("#","")
    inputwords=inputwords.replace("$","")
    inputwords=inputwords.replace("@","")
    inputwords=inputwords.replace("%","")
    inputwords=inputwords.replace("*","")
    inputwords=inputwords.replace("&","")
    inputwords=inputwords.split()
    mostlikely=["",0]
    for word in inputwords:
        for wordset in dataset:
            for words in dataset[wordset]:
                if word==words:
                    try:
                        dataset[wordset][len(dataset[wordset])-1]+=1
                    except:
                        dataset[wordset].append(0)
                        dataset[wordset][len(dataset[wordset])-1]+=1
                    if dataset[wordset][len(dataset[wordset])-1]>mostlikely[1]:
                        mostlikely[1]=dataset[wordset][len(dataset[wordset])-1]
                        mostlikely[0]=wordset
    try:
        response=responses[mostlikely[0]][random.randint(0,len(responses[mostlikely[0]])-1)]
    except:
        response="takesecondinput"
    return(response)
def smart(prev,ans):
    key=""
    for x in range (0,10):
        key=key+str(random.randint(0,9))
    prev=prev.lower()
    prev=prev.split()
    file=json.load(open('typefinder.json','r'))
    file[key]=[]
    for words in prev:
        file[key].append(words)
    json.dump(file,open('typefinder.json','w'))  
    file=json.load(open('responses.json','r'))
    file[key]=[]
    file[key].append(ans)
    json.dump(file,open('responses.json','w'))  