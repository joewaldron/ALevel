'''
Anything written here is called a comment - the computer ignores it,
so this lets you explain what your code does.
This type of comment can have as many lines as you like, as long as
it is between the sets of three apostrophes.
'''

# Comments can also look like this, starting with a hash symbol.
# Useful if something doesn't work and you want to ask for advice!


name = input("Please enter your name:")
print("Well hello,", name)

if name.find('s') > 0:
    print("did you know you have an 's' in your name?")
    # It is important to use the tab key for any instructions that need to happen only if the above condition is true
    # This is how Python knows which bits of your code need to be run in which order.
else:
    print("There's no 's' in your name!")

country = input("please tell me what country you're from... ")
nexta = input("Shall I tell you the capital? Please write 'y' or 'n'.")
if nexta == "y" or nexta == "Y":
    print("the capital of", country, "is...", country.upper()[0], "! Aren't I clever ;)?")
elif nexta == "n" or nexta == "N":  # elif stands for else, if - it's shorter!
    print("oh go on.")				# to understand how this works, try to run the program and get all of these outputs.
else:
    print("I didn't understand that...")

'''
I have used some other functions here which I am sure you can work out what they do by running this code!

Below you can write your quiz questions as per the task...
'''