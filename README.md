
# UltimateAnalyticsBenchmark
To get a score on system performace of your machine in the field of analytics

#Introduction

##Methodology
It works by calculating various statistical values and models (explained later) and compares with a base and it uses Hyperbolic curve formulae which highly penalizes slow machines and at the same time highly rewards good machines. 


##Score Range
Theoratically score will range from [0, infi)

#Functions used

##Generating list
Using numpy to generate a very large list of random floats

*The folwing functions are run several times and score is calculated*

##Sorting the List
Using self implemented quicksort to sort.

##Min
Finding the minimum element of the list.

##Max
Finding the max element of the lis.

##Mean
Finding the mean of the list.

##Standard Deviation 
Finding the sample standard deviation of the list

##Kurtosis
Finding the excess Kurtosis of the list

##Pandas Analysis and Training several models
The sample data in the "Data/data.xlsx" file is used as the sample data and various operations are performed on the data and the following models are trained:
###1)Ordinary Least Sqaure
###2)Weighted Least Square
###3)GLSAR (Generalized least square with AR(p) convergence)
###4)Robust Linear Model

#Dependency
1)statsmodels
2)pandas

*Except models all methods are self implemented, so not much dependency is there*

