import random
custDB=[["0764648342","Jose",20000,6969],["0764748382","Joes",265000,9679]]
def process_transaction(sender,reciever,amountsent,db):
    global custDB
    custDB = db
    code=Transaction_number()
    move_money(sender,reciever,amountsent)
    return code
def Transaction_number():
    num=random.randint(0,10000000000)
    return num
def move_money (sender,reciever,amountsent):
     global custDB
     custDB[sender][2]
     custDB[reciever][2]
     custDB[sender][2]=custDB[sender][2]-amountsent
     custDB[reciever][2]=custDB[reciever][2]+amountsent
#process_transaction(0,1,6986567484848486)


'''
move_money(0,1,6969)
print(custDB)
code=Transaction_number()
print(code)
'''
