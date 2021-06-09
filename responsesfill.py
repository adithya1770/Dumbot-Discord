import json
Type=json.load(open('responses.json','r'))
def fillresponse(inp,ex):
    Type=json.load(open('responses.json','r'))
    Type[inp]=[]
    ex=ex.replace("?","")
    ex=ex.replace("!","")
    ex=ex.replace("#","")
    ex=ex.replace("$","")
    ex=ex.replace("@","")
    ex=ex.replace("%","")
    ex=ex.replace("*","")
    ex=ex.replace("&","")
    ex=ex.replace("/","")
    Type[inp].append(ex)
    json.dump(Type,open('responses.json','w'))