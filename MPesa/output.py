custDB = [["0796299991","yang",0,1234]]

def output(sender_id,reciver_id,amountsent,transation,db):
    global custDB
    custDB = db
    sender(amountsent,reciver_id,transation)
    reciver(amountsent,sender_id,transation)
def sender(amount,reciver_name,transation):
    print(custDB[reciver_name][1],"has recived",amount,"transation number",transation)
def reciver(amount,sender_name,transation):
    print(custDB[sender_name][1],"has sent",amount,"transation number",transation)


#output(0,0,9,8)
