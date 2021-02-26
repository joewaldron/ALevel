def sumDigits(data):
    total = 0
    secondFlag = False
    for i in reversed(data):
        i = int(i)
        if secondFlag:
            i*=2
            secondFlag = False
        else:
            secondFlag = True
        while i > 9:
            digitTotal = 0
            for j in str(i):
                digitTotal += int(j)
            i = digitTotal
        total += i
    return total

option = "1"
while int(option) > 0:
    option = input("1 to verify, 2 to calc, 0 to exit: ")
    if int(option) == 1:
        num = input("Pls enter the number to verify: ")
        result = sumDigits(num)
        if result % 10 == 0:
            print("Valid")
        else:
            print("Invalid")

    elif int(option) == 2:
        num = input("Pls enter the number to calculate a check digit for: ")
        result = sumDigits(num+"0")
        result = (result*9) % 10
        print("The check digit is", result)
