def solution(string,markers):
    #your code here
    newString = ''
    stringList = string.split("\n")
    newList = []
    for s in stringList:
        for marker in markers:
            if(marker in s):
                newString += s[:s.index(marker)]
                if(newString[len(newString)-1] == ' '):
                    newString = newString[:len(newString)-1]+'\n'
                #newString += '\n'
            elif(marker not in s):
                for m in markers:
                    if(m not in s and m != marker and s not in newList):
                        newList = s.split("\n")
                        newString += newList[0] + "\n"
    newString = newString[:-1]
    return newString
