from utils.functionality import sort1
from utils.stats import max, min, mean, kurtosis, sd
from utils.predict import modelTraining
from utils.helper import myTimeFunc, listSize, globalTimeLis, calculateScore
import numpy as np



globalTimeStart = myTimeFunc()



print("Generating random list with {} elements".format(listSize))
timeListCreationStart = myTimeFunc()
li = list(np.random.random(listSize*100))
del li
li = list(np.random.random(listSize))
endTime = myTimeFunc()-timeListCreationStart
globalTimeLis.append(endTime)
print("Time taken to generate the list is {} seconds".format(endTime))



print("Sorting the generated list")
sort1(li)
print("*************************")

print("Finding the min of the list")
min(li)
print("*************************")

print("Finding the max of the list")
max(li)
print("*************************")

print("Finding the mean of the list")
mean(li)
print("*************************")

print("Finding the Standard Deviation of the list")
sd(li)
print("*************************")

print("Finding the kurtosis of the list")
kurtosis(li)
print("*************************")

print("Training the models")
modelTraining()
print("*************************")


print("Total time taken for it to run is {} seconds".format(myTimeFunc()-globalTimeStart))
calculateScore()