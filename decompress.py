import re

def decompress(s):
    subStr = []
    compr = re.findall(r'\d+x\w', s)
    splitUp = re.split(r'\d+x\w', s)
    print compr, splitUp
    for i, c in enumerate(compr):
        numRep = re.findall(r'\d+', c)
        numRep = int(numRep[0])
        subStr.append(numRep * c[-1])
    print subStr
    res = splitUp[0]
    for i in range(len(splitUp)-1):
        res = res+subStr[i] + splitUp[i+1]
    
    return res

print decompress('aa12xErtgvd5xrghrtsadf')