from utils.helper import timeRepeaterLi

def compare(a, b, desc):
    """
    This is to compare two values
    :param a: any float or integer
    :param b: any float or integer
    :param desc: If true, gives the result to make the array in descending order
    :return:
    """
    if not desc:
        return a <= b
    else:
        return a > b


def swap(li, i, j):
    """
    This is to swap two elements within a list
    :param li: a list
    :param i: index of 1st element
    :param j: index of 2nd element
    :return:
    """
    tmp = li[i]
    li[i] = li[j]
    li[j] = tmp


def partition(li, start, end, desc):
    """
    This function is to partition the list so that it will be helpful for quickSort
    :param li: list
    :param start: start index
    :param end: end index
    :param desc: True if you want it in descending order or ascending
    :return: index of pivot
    """
    pivot = li[end]
    lo = start
    for i in range(start, end):
        if compare(li[i], pivot, desc):
            swap(li, i, lo)
            lo += 1
    swap(li, lo, end)
    return lo


def qsort(li, lo, hi, desc):
    """
    This is qsort function which has O(n^2) and o(nlogn) time complexity and effective space complexity of o(n)
    :param li: list
    :param lo: first index
    :param hi: last index
    :param desc: True if you want it in descending order or ascending
    :return: None
    """
    if len(li[lo:(hi + 1)]) <= 1:
        return
    p = partition(li, lo, hi, desc)
    qsort(li, lo, p-1, desc)
    qsort(li, p+1, hi, desc)

@timeRepeaterLi
def sort1(li, lo=0, hi=0, desc=True):
    """
    This is just wrapper around qsort to give some default values. For more info see qsort
    :param li: list
    :param lo: lower value defaults to 0
    :param hi: higher value defaults to last index of list
    :param desc: default True, explicitly needs to mention False to get ascending
    :return: None
    """
    if hi == 0:
        hi = len(li)-1
    qsort(li, lo, hi, desc)

@timeRepeaterLi
def removeDups(li):
    """
    This is a hack to remove the duplicates from a list, By using a default dataset
    :param li: list whose duplicates you want to remove
    :return: de-duplicated data
    """
    k = set(li) #set is a default datatype in python, it is used to check union and intersection of various arrays, this is an exploit of it :P
    return list(k)

@timeRepeaterLi
def removeDups2(li):
    """
    This is the other method to remove the duplicates with time complexity of O(n)
    This is same as removeDups because as in dictionary (used here) set also stores based on
    the hash value of the element
    :param li: list
    :return: de-duplicated data
    """
    di = {}
    for k in li:
        try :
            di[k]
        except KeyError :
            di[k]=0
    return list(di.keys())

@timeRepeaterLi
def findIndex(li, elem):
    """
    This is used to find the index of element
    :param li: list
    :param elem: element to find
    :return: the index or raises Exception if not found, needs to be handled properly
    """
    for i in range(0, len(li)):
        if li[i] == elem:
            return i

    raise Exception

