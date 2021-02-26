import random
import sys
        #phone num      name     bal     pin
CustDb = [["0790509803", "Ryan", "1000", "0000"],
          ["0722333897", "Ivan",  "2000", "1111"]]

def getCustomerData(db):
    global CustDb
    CustDb = db
    cust,recv = phone_no()
    pin(cust)
    amount = input_amount(cust)
    return [cust,recv,amount]



def phone_no():
    print("Please Input Customer Number")
    usernumber = input()
    pos = 0
    found = False
    while (pos < len(CustDb)):
        if usernumber == CustDb [pos][0]:
            found = True
            CustID = pos
            break
        else:
            pos = pos + 1


    print("Please Input Receiver's Number")
    receivernumber = input()

    rpos = 0
    foundreceiver = False
    while(pos < len(CustDb)):
        if usernumber == CustDb [pos][0]:
            foundreceiver = True
            ReceiverID = rpos
            break
        else:
            rpos = rpos + 1

    return CustID, ReceiverID





def pin(CustID):
    attempts = 3
    global CustDb

    for i in range (0,3):
        print("Please enter your pin - You have", attempts )
        userpin = int(input())

        if userpin == CustDb[CustID][3]:
            print("Pin entered successfully")
            break
        else:
             attempts = attempts -1


    if attempts == 0:
             sys.exit('Your account has been blocked for security purposes')

def input_amount (CustID):
    global CustDb
    print("Please enter amount")
    amount = int(input())

    if amount >  CustDb[CustID][2]:
            print("insufficient amount")
    else:
            print(" Go to next Step")

    return amount

#main program




