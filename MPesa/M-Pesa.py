import random
import output
import processmp
import InputMpesa

custDB = []
database = open("Safaricom.txt", "w")

for i in range(50):
    phonenum = "07"
    for j in range(8):
        phonenum += str(random.randint(0,9))
    custname = random.choice(["Ryan","Anthony","Ivan","Yang","Maliki","John","Josef","Edwin","Lacktano","Michael","Simon","Isaac","Yuvraj","Riya"])
    pin = random.randint(1000,9999)
    bal = random.randint(0,50000)
    newcustomer = [phonenum,custname,bal,pin]
    custDB.append(newcustomer)
    database.writelines(str(newcustomer) + "\n")
database.close()

trans_data = InputMpesa.getCustomerData(custDB)
##trans_data is sender,receiver,amount
tnum = processmp.process_transaction(trans_data[0],trans_data[1],trans_data[2],custDB)
output.output(trans_data[0],trans_data[1],trans_data[2],tnum,custDB)
#output.output(5,36,200,1,custDB)
