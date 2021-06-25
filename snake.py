from microbit import *
import random
#microbit snake experiment

queue = [  ]
score = 0
#will use pop() to remove head, insert(0) to add tail.

#initial test with three coordinate sets
startpos = [2,2]
queue.insert(0,startpos)
hungry = True
grow = False

while True:
    badc = []
    #draw the snake
    for eachpos in queue:
        display.set_pixel(eachpos[0],eachpos[1],9)
    #generate random food
    if hungry:
        rand_x = random.randint(0,4)
        rand_y = random.randint(0,4)
        while [rand_x,rand_y] in queue:
            rand_x = random.randint(0,4)
            rand_y = random.randint(0,4)
        display.set_pixel(rand_x,rand_y,5)
        hungry = False

    #determine the direction
    direction = ""
    x_acc = accelerometer.get_x()
    y_acc = accelerometer.get_y()
    if x_acc > 25 and x_acc > abs(y_acc):
        direction = "E"
    elif x_acc < -25 and abs(x_acc) > abs(y_acc):
        direction = "W"
    if y_acc > 25 and y_acc > abs(x_acc):
        direction = "S"
    elif y_acc < -25 and abs(y_acc) > abs(x_acc):
        direction = "N"

    #move the snake - append next position to queue, remove head
    nextpos = [0,0]
    nextpos[0] = queue[0][0]
    nextpos[1] = queue[0][1]
    if direction == "N":
        nextpos[1] -= 1
        if nextpos[1] < 0: nextpos[1] = 4
    elif direction == "E":
        nextpos[0] += 1
        if nextpos[0] > 4: nextpos[0] = 0
    if direction == "S":
        nextpos[1] += 1
        if nextpos[1] > 4: nextpos[1] = 0
    elif direction == "W":
        nextpos[0] -= 1
        if nextpos[0] < 0: nextpos[0] = 4
    #else:
        #no change to nextpos!
    print(direction,queue)
    queue.insert(0,nextpos)
    if nextpos[0] == rand_x and nextpos[1] == rand_y:
        score += 1
        hungry = True
        grow = True
    sleep(500)
    if not grow:
        rem = queue.pop()
    else:
        grow = False
    display.set_pixel(rem[0],rem[1],0)

