
# UltimateAnalyticsBenchmark
To get a score on system performace of your machine in the field of analytics

#Running the benchmark
* Clone or Download this repo
* cd to the cloned or Downloaded(Might need to unzip if downloaded) repo
*  issue python run.py from commandline

**If running this code on bash on ubuntu on windows, you need to do export KMP_AFFINITY=disabled**

#Requirements
* Python 3.5 or above
* statsmodels
* pandas
* numpy-mkl
**Best way to run this is install Anaconda 3 from Continuum Analytics and run it **


*Some Scores:*
####System 1:
1.	OS: Ubuntu
2.	Processor: intel i5-5th gen MQ processor
3.	Ram:- 8 GB DDR3
4.	System Type: Desktop
5.	**Score : 5.6**

####System 2:
1.	OS: Windows 10
2.	Processor: intel i5-6th gen U processor
3.	Ram: 8 GB
4.	System Type: Laptop
5.	**Score: 2.5**


####System 3:
1.	OS: Ubuntu on Windows 10 (After anniversary update)
2.	Processor: intel i5-5th gen U processor
3.	Ram: 12 GB
4.	System Type: Laptop
5.	**Score: 2.15**

####System 4:
1.	OS: Windows 10
2.	Processor: intel i5-5th gen U processor
3.	Ram: 12 GB
4.	System Type: Laptop
5.	**Score: 2.0**

####System 5:
1.	OS: Windows 10
2.	Processor: intel i3-5th gen U processor
3.	Ram: 4 GB
4.	System Type: Laptop
5.	**Score: 1.3**




#Introduction

##Methodology
It works by calculating various statistical values and models (explained later) and compares with a base and it uses Hyperbolic curve formulae which highly penalizes slow machines and at the same time highly rewards good machines. 


##Score Range
Theoratically score will range from [0, infi)

##Python version
Built using python 3


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




*Except model creation, all methods are self implemented*

