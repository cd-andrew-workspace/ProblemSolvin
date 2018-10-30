def problem03(s):
    myDict = {}
    for term in s:
        if term in myDict:
            myDict[term] += 1
        else:
            myDict[term] = 1
    return myDict
print(problem03("Test String"))
