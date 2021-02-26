# Bubble sort algorithm
# Loop through from the start to the end
# Compare adjacent numbers in the list
# If the lefthand number is bigger than the righthand number, swap them
# Otherwise, leave them as they are
# Go back to line 3 to check the next two numbers
# When all have been compared, go back to line 2 to check again until all are in order.
numbers = [5,4,3,2,1]
# after first shuffle (complete loop 2-6)
numbers1 = [4,3,2,1,5]
#after 2nd shuffle
numbers2 = [3,2,1,4,5]
# after 3rd shuffle
numbers3 = [2,1,3,4,5]
# in the worst case for bubble sort you need to repeat the whole process n times
# Each time, you need to compare every item in the list, in other words n comparisons
# The worst case running time will be n x n comparisons.
numbers = []
import random, time
for n in range(500):
    number = random.randint(1,500)
    numbers.append(number)
print(numbers)
numbers2 = numbers.copy()
numbers3 = numbers.copy()
starttime2 = time.time()
numbers2.sort()
endtime2 = time.time()
# Sort numbers into ascending order using bubble sort. Iterative solution.
# Please don't worry about the recursive solution for now - leave this for Y13
comparisons = 0
starttime = time.time()
for i in range(len(numbers)-1):
    for j in range(len(numbers)-1):  # j will represent the POSITION not the DATA
        # check the first two items
        if numbers[j] > numbers [j+1]:
            # swap
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
            #print(numbers)
        comparisons += 1
endtime = time.time()
print(numbers)
# This implementation is an 'Isaac' algorithm. It works, but it's not PERFECT.

comparisons2 = 0
starttime3 = time.time()
numbers_to_check = len(numbers3)-1
for i in range(len(numbers3)-1):
    anymoreswaps = False
    for j in range(numbers_to_check):  # j will represent the POSITION not the DATA
        # check the first two items
        if numbers3[j] > numbers3 [j+1]:
            # swap
            temp = numbers3[j]
            numbers3[j] = numbers3[j+1]
            numbers3[j+1] = temp
            anymoreswaps = True
        comparisons2 += 1   #This works, and is better, but isn't perfect!!
    if not anymoreswaps:
        break
    numbers_to_check -=1
endtime3 = time.time()

print("Number of comparisons (Isaac) needed:",comparisons)
print("Time needed to sort (Bubble Isaac):",endtime-starttime,"s")
print("Number of comparisons (Optimised) needed:",comparisons2)
print("Time needed to sort (Bubble Optimised):",endtime3-starttime3,"s")
print("Time needed to sort (Tim):",endtime2-starttime2,"s")
