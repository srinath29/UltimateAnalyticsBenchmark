import time

scoreLis = [0.0001,1.15,0.000001,0.000001,0.00001, 0.0001, 0.001,0.4] #expected scores or benchmark scores

myTimeFunc = time.monotonic #time function I used throughout the code
numTimes = 100 #NumTimes the function should run
listSize = 100000 #size of the random list needs to be generated so for further computation
fullScoreLis = [numTimes*i for i in scoreLis] #assuming a linear increase in time requirement with number of times a method computes
globalTimeLis = []  #a list where the time will be stored


def timeRepeater(func):
    """
    It is a decorator to the existing functions to compute it numTimes and check the time
    :param func: function which needs to be decorated
    :return: None
    """
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
    """
    Another decorator which will be used for running the func 100 times but passing a copy of the list generated previously
    :param func: the function which should be decorated
    :return: None
    """
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
    """
    The final calculator of the score
    :return: None
    """

    global globalTimeLis
    globalTimeLis = [cal if cal!=0 else fullFix for fullFix, cal in zip(fullScoreLis,globalTimeLis)]
    calc = [(fullFix/cal) for fix, fullFix, cal in zip(scoreLis, fullScoreLis, globalTimeLis)]
    print("Score for this system is {}".format(sum(calc)))