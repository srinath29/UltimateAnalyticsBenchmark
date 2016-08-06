import time

scoreLis = [0.0001,1.15,0.000001,0.000001,0.00001, 0.0001, 0.001,0.4]

myTimeFunc = time.monotonic
numTimes = 10
listSize = 100000
fullScoreLis = [numTimes*i for i in scoreLis]
globalTimeLis = []
def timeRepeater(func):
    def runAgainAndAgain():
        timeStart = myTimeFunc()
        for i in range(numTimes):
            if i == 1:
                print("-->For the first run the time it took is {} seconds".format(myTimeFunc()-timeStart))
            func()
            endTime = myTimeFunc()-timeStart
        print("-->Time taken to run {} times is {} seconds".format(numTimes, endTime))
        globalTimeLis.append(endTime)
    return runAgainAndAgain


def timeRepeaterLi(func):
    def runAgainAndAgain(li):
        timeStart = myTimeFunc()
        for i in range(numTimes):
            if i == 1:
                print("-->For the first run the time it took is {} seconds".format(myTimeFunc()-timeStart))
            func(li[:])
        endTime = myTimeFunc() - timeStart
        print("-->Time taken to run {} times is {} seconds".format(numTimes, endTime))
        globalTimeLis.append(endTime)
    return runAgainAndAgain


def calculateScore():
    global globalTimeLis
    globalTimeLis = [ cal if cal!=0 else fullFix for fullFix, cal in zip(fullScoreLis,globalTimeLis) ]
    calc = [ (fullFix/cal) for fix, fullFix, cal in zip(scoreLis, fullScoreLis, globalTimeLis)]
    print("Score for this system is {}".format(sum(calc)))