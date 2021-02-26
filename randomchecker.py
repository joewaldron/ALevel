import random

Repetitions = 202020   # integer
RandomNumFrequencies = []  # empty array
for i in range(11):
    RandomNumFrequencies.append(0) # initialise array with 10 zero integers
# Positions 0-10
#[0    ,0,2,1,0,2,0,0,0,0,1]

for i in range(Repetitions):
    rnum = random.randint(1, 10)
    RandomNumFrequencies[rnum] += 1
print(RandomNumFrequencies)

ExpectedFrequency = Repetitions / 10 # round() #int() #//

print("The expected frequency is", ExpectedFrequency)
print("Number    Frequency    Difference")

# for each element in the RandomNumFrequencies from pos 1 to 10,
for pos in range(1,11):
    # print out the position , print out the value (count), print value-ExpectedFrequency (difference)
    print(pos, "        ", RandomNumFrequencies[pos], "         ", RandomNumFrequencies[pos]-ExpectedFrequency)

