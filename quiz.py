import sys
import operator

"""
/*
*************************
*AHMET SERDAR GEZE       *
*SOFTWARE DEVOLOPER      *
*                        *
*                        *
*                        *
*                        *
*                        *
*************************

*/


"""

dataFile = open('WBC.data', 'r').read()
dataDic = {i.split(',')[0]: i.split(',')[1:] for i in dataFile.split('\n')}

dataFile2 = open('WBC.data', 'r').read()
dataDic2 = {i.split(',')[0]: i.split(',')[1:] for i in dataFile.split('\n')}


# benign
# malignant
def funDataClean():
    malig = []
    bening = []
    nonQuestMalig = []
    questMalig = []
    nonQuestBening = []
    questBening = []
    for key in dataDic:
        variable = dataDic[key]
        variable.append(key)
        if "malignant" in variable:
            malig.append(variable)
            if "?" in variable:
                questMalig.append(variable)
            else:
                nonQuestMalig.append(variable)
        elif "benign" in variable:
            bening.append(variable)
            if "?" in variable:
                questBening.append(variable)
            else:
                nonQuestBening.append(variable)

    globalSum = 0
    for item in questMalig:
        questIndex = item.index("?")
        count = 0
        sum = 0
        avarage = 0
        for itemOfAllMalig in malig:
            if itemOfAllMalig[questIndex] != "?":
                sum += int(itemOfAllMalig[questIndex])
                count += 1
        avarage = sum / count
        globalSum += round(avarage)
        item.append(round(avarage))

    for item in questBening:
        questIndex = item.index("?")
        count = 0
        sum = 0
        avarage = 0
        for itemOfAllMalig in bening:
            if itemOfAllMalig[questIndex] != "?":
                sum += int(itemOfAllMalig[questIndex])
                count += 1
        avarage = sum / count
        globalSum += round(avarage)
        item.append(round(avarage))

    globalLength = len(questBening) + len(questMalig)
    return globalSum / globalLength




def performStepWiseSearch():
    filter = sys.argv[1].split(',')
    print(filter)
    allItems = []
    for key in dataDic2:
        allItems.append(dataDic2[key])

    operators = {
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
        "!=": operator.ne,
        "=": operator.eq

    }
    a=0
    print(filter)
    resultArr = []
    for item in allItems:
        expectedArr = []
        i = 0
        for op in filter:
            exp = op.split(':')
            if len(exp) == 1:
                expectedArr.append(True)
            else:
                if item[i] != "?":
                    expression=op.split(':')
                    localResult= operators.get(expression[0])(int(item[i]),int(expression[1]))
                    if localResult:
                        expectedArr.append(True)
                    else:
                        expectedArr.append(False)
                else:
                    expectedArr.append(False)
            i += 1

        flag=True
        for ele in expectedArr:
            if ele==False:
                flag=False

        if flag==True:
            resultArr.append(item)

    beningC=0
    malignantC=0
    for item in resultArr:
        if item[-1]=="malignant":
            malignantC+=1
        else:
            beningC+=1

    print("beningC",beningC)
    print("malig",malignantC)
    print(len(filter))
    return [beningC,malignantC]

testResult=performStepWiseSearch()
testResultav=testResult[1]/(testResult[1]+testResult[0])

# 1st phase: Cleaning WBC Database

print('The average of all missing values is  : ' + '{0:.4f}'.format(funDataClean()))

# 2nd phase: Retrieving knowledge from WBC dataset

print('\nTest Results:\n'
      '----------------------------------------------'
      '\nPositive (malignant) cases            : ' + str(testResult[1]) +
      '\nNegative (benign) cases               : ' + str(testResult[0]) +
      '\nThe probability of being positive     : ' + '{0:.4f}'.format(testResultav) +
      '\n----------------------------------------------')
