import turtle
import time

def initialise():
    canvas = turtle.Screen()
    canvas.title("Flag-It")
    soup = turtle.Turtle()
    soup.penup()
    soup.color("hotpink")
    return soup

#create functions here to draw lines and then functions to call these for the various numbers in your barcode.


pen = initialise()

time.sleep(5)
