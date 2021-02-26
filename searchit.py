

data = [1,2,3,4,5,67,300,3000]

# Linear search to find position of 300
pos = 0
found = False
while pos < len(data):
    if data[pos] == 300:
        found = True
        print(pos)
        break
    pos += 1

# Binary search
mini = 0
maxi = len(data)-1
number_to_find = 15
guesses = 0
found = False
while mini <= maxi:
    guesses = guesses + 1
    nextpos = mini+ ((maxi-mini) // 2)
    if data[nextpos] == number_to_find:
        print("Got it, position",nextpos,". Number of guesses",guesses)
        found = True
        break
    elif data[nextpos] > number_to_find:
        maxi = nextpos - 1
    elif data[nextpos] < number_to_find:
        mini = nextpos + 1

if not found:
    print("Not Found. Guesses tried:", guesses)

