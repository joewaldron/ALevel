''''''
'''
Declare and initialise a 1D array of length 20
with random real numbers between -65 and 65.
'''
import random
import time
temperatures = []

for x in range(2000):
    temperatures.append(random.randint(-65,65)+random.random())
print(temperatures)
temperatures2 = temperatures.copy()
starttime = time.time()
'''
Write three functions to sort this array implementing
bubble sort, insertion sort and optionally, bogo sort.
Test each function and output the sorted list.
'''
l = 0
maxiterations = len(temperatures)
while l < len(temperatures):
    pos = 0
    maxiterations -= 1
    while pos < maxiterations:
        if temperatures[pos] > temperatures[pos+1]:
            swap = temperatures[pos]
            temperatures[pos] = temperatures[pos+1]
            temperatures[pos + 1] = swap

        pos += 1
    l += 1
endtime = time.time()
print(temperatures)
print(endtime - starttime, "s")
starttime = time.time()
pos = 1
while pos < len(temperatures2):
    innerpos = pos
    while temperatures2[innerpos] < temperatures2[innerpos - 1] and innerpos > 0:
        temp = temperatures2[innerpos-1]
        temperatures2[innerpos-1] = temperatures2[innerpos]
        temperatures2[innerpos] = temp
        innerpos -= 1
    pos += 1
endtime = time.time()
print(temperatures2)
print(endtime - starttime, "s")

'''
Output the time needed for each function to sort the arrays.

Change the array to contain 20 thousand (10^3) numbers and time the functions again.

Extension: improve your password checker using a binary search. Output how many tries
and how much time is needed to find the password for both linear and binary search.
'''
