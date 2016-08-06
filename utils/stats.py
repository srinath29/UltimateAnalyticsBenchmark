from utils.helper import timeRepeaterLi


def meanWD(li):
    """
    This will return the mean value of the data
    :param li: list of values
    :return: mean of data
    """
    suma = 0
    for p in li:
        suma = suma+p
    return suma/float(len(li))


def sdWD(li, sample=True):
    """
    This will return the standard deviation of the data
    :param li: list of values
    :param sample: Default True, which will calculate the sample standard deviation else population standard deviation
    :return: Standard Deviation of the data
    """
    meani = meanWD(li)
    suma = 0
    if sample:
        n= len(li)-1
    else:
        n=len(li)
    for p in li:
        tmp = (p-meani) ** 2
        suma += tmp
    return (suma/n) ** 0.5


@timeRepeaterLi
def min(li):
    """
    This will return the minimum value in the dataset
    :param li: list of values
    :return: minimum value
    """
    mini = li[0]
    for p in li:
        if p < mini:
            mini = p
    return mini

@timeRepeaterLi
def max(li):
    """
    This will return the max of data set
    :param li: list of values
    :return: element with max value
    """
    maxim = li[0]
    for p in li:
        if p > maxim:
            maxim = p
    return maxim

@timeRepeaterLi
def mean(li):
    """
    This will return the mean value of the data
    :param li: list of values
    :return: mean of data
    """
    suma = 0
    for p in li:
        suma = suma+p
    return suma/float(len(li))

@timeRepeaterLi
def sd(li, sample=True):
    """
    This will return the standard deviation of the data
    :param li: list of values
    :param sample: Default True, which will calculate the sample standard deviation else population standard deviation
    :return: Standard Deviation of the data
    """
    meani = meanWD(li)
    suma = 0
    if sample:
        n= len(li)-1
    else:
        n=len(li)
    for p in li:
        tmp = (p-meani) ** 2
        suma += tmp
    return (suma/n) ** 0.5

@timeRepeaterLi
def kurtosis(li, excess=True):
    """
    Returns the peakness of the data
    :param li: list of values
    :param excess: Default true, returns the excess of the kurtosis value else the absolute value
    :return: calculated kurtosis value
    """
    suma = 0
    meani = meanWD(li)
    sD = sdWD(li)
    n = len(li)
    sampleAdjustment = (n*(n+1))/((n-1)*(n-2)*(n-3))
    sampleExcess = 3*((n-1)**2)/((n-2)*(n-3))
    for p in li:
        tmp = (p-meani)**4
        suma += tmp
    ans = (sampleAdjustment*suma)/(sD**4)
    if excess:
        ans-=sampleExcess
    return ans

